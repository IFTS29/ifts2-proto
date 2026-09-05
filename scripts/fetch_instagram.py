#!/usr/bin/env py
"""
fetch_instagram.py
==================
Pipeline de sincronización automatizada para el IFTS N° 2.
Consume la Instagram API with Instagram Login (graph.instagram.com),
descarga las imágenes localmente para neutralizar el vencimiento de 48-72hs,
clasifica por hashtags institucionales y genera el feed JSON estático.

Costo de ejecución: $0 (pensado para correr en GitHub Actions).
"""

import os
import re
import json
import urllib.request
import urllib.error
from datetime import datetime

# Rutas de salida en el proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DATA_FILE = os.path.join(BASE_DIR, "data", "instagram-feed.json")
OUTPUT_IMAGES_DIR = os.path.join(BASE_DIR, "public", "assets", "instagram")

# Mapeo de hashtags a categorías de la interfaz
HASHTAG_CATEGORY_MAP = {
    "emprendimientos": ["#emprendimientos", "#emprendedores", "#negociogastronomico", "#ifts2emprende"],
    "masterclass": ["#masterclass", "#claseespecial", "#enologia", "#chocolateria", "#pasteleria"],
    "cocina": ["#practicas", "#brigada", "#cocina", "#tecnicasculinarias", "#taller"],
    "eventos": ["#eventos", "#guisofest", "#concurso", "#colacion", "#nochedelosmuseos"]
}

def ensure_directories():
    os.makedirs(os.path.dirname(OUTPUT_DATA_FILE), exist_ok=True)
    os.makedirs(OUTPUT_IMAGES_DIR, exist_ok=True)

def determine_category(caption: str) -> str:
    caption_lower = (caption or "").lower()
    for category, tags in HASHTAG_CATEGORY_MAP.items():
        if any(tag in caption_lower for tag in tags):
            return category
    return "general"

def download_image(url: str, output_path: str) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "IFTS2-Sync-Bot/1.0"})
        with urllib.request.urlopen(req, timeout=15) as response, open(output_path, 'wb') as out_file:
            out_file.write(response.read())
        return True
    except Exception as e:
        print(f"[-] Error al descargar imagen desde {url}: {e}")
        return False

def refresh_long_lived_token(token: str):
    """
    Renueva el token de larga duración antes de su vencimiento de 60 días.
    Endpoint oficial de Instagram API:
    GET https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token={TOKEN}
    """
    refresh_url = f"https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token={token}"
    try:
        req = urllib.request.Request(refresh_url, headers={"User-Agent": "IFTS2-Sync-Bot/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            new_token = data.get("access_token")
            expires_in = data.get("expires_in")
            print(f"[+] Token renovado con éxito. Vence en {expires_in // 86400} días.")
            return new_token
    except Exception as e:
        print(f"[-] No se pudo renovar el token: {e}")
        return None

def fetch_instagram_posts(access_token: str, limit: int = 12):
    """
    Consulta los últimos medios publicados por la cuenta institucional.
    """
    fields = "id,caption,media_type,media_url,thumbnail_url,permalink,timestamp"
    url = f"https://graph.instagram.com/me/media?fields={fields}&limit={limit}&access_token={access_token}"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "IFTS2-Sync-Bot/1.0"})
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data.get("data", [])
    except urllib.error.HTTPError as e:
        print(f"[-] Error HTTP {e.code} al consultar Instagram API: {e.read().decode('utf-8')}")
        return []
    except Exception as e:
        print(f"[-] Error inesperado al consultar Instagram API: {e}")
        return []

def run_sync():
    ensure_directories()
    token = os.environ.get("INSTAGRAM_ACCESS_TOKEN")

    if not token:
        print("[!] Advertencia: No se encontró INSTAGRAM_ACCESS_TOKEN en las variables de entorno.")
        print("[*] Generando feed de muestra para entorno local y testing del prototipo...")
        mock_posts = [
            {
                "id": "mock_1",
                "caption": "Concurso Anual de Guisos Criollos del IFTS N° 2. Estudiantes de 2° año recrearon recetas tradicionales calculando mermas y rendimientos reales. #IFTS2Eventos #GuisoFest #Cocina",
                "category": "eventos",
                "media_type": "IMAGE",
                "image_local_url": "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=800&q=80",
                "permalink": "https://instagram.com/ifts2de20",
                "timestamp": datetime.now().isoformat()
            },
            {
                "id": "mock_2",
                "caption": "Felicitamos a los egresados de la promoción 2024 que abrieron su local comercial en Caballito tras aprobar su proyecto integrador. #IFTS2Emprende #Emprendimientos #NegocioGastronomico",
                "category": "emprendimientos",
                "media_type": "IMAGE",
                "image_local_url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800&q=80",
                "permalink": "https://instagram.com/ifts2de20",
                "timestamp": datetime.now().isoformat()
            },
            {
                "id": "mock_3",
                "caption": "Masterclass de chocolatería fina y templado de precisión. Enfoque en costeo por porción y vida útil en anaquel. #IFTS2Masterclass #Pasteleria #Chocolateria",
                "category": "masterclass",
                "media_type": "IMAGE",
                "image_local_url": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80",
                "permalink": "https://instagram.com/ifts2de20",
                "timestamp": datetime.now().isoformat()
            }
        ]
        with open(OUTPUT_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({"updated_at": datetime.now().isoformat(), "posts": mock_posts}, f, indent=2, ensure_ascii=False)
        print(f"[+] Feed simulado guardado en: {OUTPUT_DATA_FILE}")
        return

    print("[*] Consultando Instagram API with Instagram Login...")
    raw_posts = fetch_instagram_posts(token)
    processed_posts = []

    for item in raw_posts:
        media_id = item.get("id")
        media_type = item.get("media_type")
        caption = item.get("caption", "")
        permalink = item.get("permalink", "https://instagram.com/ifts2de20")
        timestamp = item.get("timestamp", "")

        # Elegir URL fuente según sea video o imagen
        source_media_url = item.get("thumbnail_url") if media_type == "VIDEO" else item.get("media_url")
        if not source_media_url:
            continue

        # Descarga local para neutralizar expiración de 48-72h
        local_filename = f"{media_id}.jpg"
        local_filepath = os.path.join(OUTPUT_IMAGES_DIR, local_filename)
        success = download_image(source_media_url, local_filepath)

        category = determine_category(caption)

        processed_posts.append({
            "id": media_id,
            "caption": caption,
            "category": category,
            "media_type": media_type,
            "image_local_url": f"/assets/instagram/{local_filename}" if success else source_media_url,
            "permalink": permalink,
            "timestamp": timestamp
        })

    # Guardar archivo consolidado
    payload = {
        "updated_at": datetime.now().isoformat(),
        "total": len(processed_posts),
        "posts": processed_posts
    }

    with open(OUTPUT_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"[+] Sincronización finalizada. {len(processed_posts)} publicaciones guardadas en {OUTPUT_DATA_FILE}")

    # Chequeo de refresco de token
    refresh_long_lived_token(token)

if __name__ == "__main__":
    run_sync()
