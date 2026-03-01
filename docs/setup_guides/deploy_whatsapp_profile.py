import requests
import os
from dotenv import load_dotenv

# Configuración Inicial
load_dotenv()
META_ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_ID") # Extraído del panel de desarrolladores de Meta
API_VERSION = "v18.0"

def configure_whatsapp_profile():
    if not META_ACCESS_TOKEN or not PHONE_NUMBER_ID:
        print("Error: Credenciales de Meta faltantes en el .env (META_ACCESS_TOKEN, WHATSAPP_PHONE_ID)")
        return

    url = f"https://graph.facebook.com/{API_VERSION}/{PHONE_NUMBER_ID}/whatsapp_business_profile"
    
    headers = {
        "Authorization": f"Bearer {META_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # Datos oficiales del Operations Commander
    profile_data = {
        "messaging_product": "whatsapp",
        "about": "Boutique definitiva del calzado premium en Venezuela. 🇻🇪 Calidad internacional, estética de vanguardia. Envío seguro a nivel nacional.",
        "address": "San Cristóbal, Edo. Táchira, Venezuela",
        "description": "Descubre VORA Elite. Seleccionamos cuidadosamente calzado de lujo, desde urban sneakers de diseño exclusivo hasta tacones de alta costura, pensados para quienes exigen excelencia y sofisticación en cada paso.",
        "email": "contacto@voraelite.com",
        "websites": [
            "https://klarx94-architect.github.io/Zapatosproject/", # VORA Ecosystem Demo / Landing
            "https://instagram.com/voraelite"
        ],
        "vertical": "APPAREL" # Categoría: Ropa / Calzado
    }

    print("Configurando el Perfil de Empresa en WhatsApp Cloud API...")
    try:
        response = requests.post(url, headers=headers, json=profile_data)
        if response.status_code == 200:
            print("¡Éxito! Perfil de WhatsApp actualizado correctamente a la identidad VORA Elite.")
            print("Tu número +58 416-3794800 ahora mostrará la información oficial a cada lead.")
        else:
            print(f"Error en la petición: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Falla de conexión: {e}")

if __name__ == "__main__":
    configure_whatsapp_profile()
