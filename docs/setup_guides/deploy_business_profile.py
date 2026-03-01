import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes indicados por directriz
SCOPES = ['https://www.googleapis.com/auth/business.manage']

def get_credentials():
    creds = None
    brand_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../brand'))
    creds_path = os.path.join(brand_dir, 'credentials.json')
    token_path = os.path.join(brand_dir, 'token.json')
    
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
            
    return creds

def deploy_vora_profile():
    print("Iniciando despliegue de perfil Google Business: VORA Elite...")
    creds = get_credentials()
    
    # IMPORTANTE: Google My Business API v4/v1 difiere, se asume estructura general para My Business Business Information API
    service = build('mybusinessbusinessinformation', 'v1', credentials=creds)
    
    # 1. Obtener la cuenta asociada al usuario
    account_service = build('mybusinessaccountmanagement', 'v1', credentials=creds)
    accounts = account_service.accounts().list().execute()
    
    if not accounts.get('accounts'):
        print("Error: No se encontró cuenta de Google Business asociada.")
        return
        
    account_name = accounts['accounts'][0]['name']
    
    # Configuración estricta dictada por el Operations Commander
    location_data = {
        "title": "VORA Elite", # Sin Keyword Stuffing
        "categories": {
            "primaryCategory": {
                "name": "gcid:shoe_store" # Shoe store (Zapatería)
            }
        },
        "storefrontAddress": {
            "regionCode": "VE",
            "languageCode": "es",
            "locality": "Cordero",
            "administrativeArea": "Táchira",
            "addressLines": ["San Cristóbal, Edo. Táchira"] # Solo registro interno
        },
        "serviceArea": {
            "businessType": "CUSTOMER_LOCATION_ONLY", # Service Area Business (SAB), hasFixedLocation=False
            "places": {
                "placeInfos": [
                    {
                        "placeId": "ChIJcQpd22h0aYwRg2lQ8Xf56Q8", # Place ID genérico para Venezuela
                        "placeName": "Venezuela"
                    }
                ]
            }
        },
        "phoneNumbers": {
            "primaryPhone": "+584120000000" # Formato internacional. REEMPLAZAR CON NUMERO REAL.
        },
        "profile": {
            "description": "Descubre VORA Elite, la boutique definitiva en Cordero, Táchira, donde la calidad internacional y la estética de vanguardia convergen. Seleccionamos cuidadosamente calzado de lujo, desde urban sneakers de diseño exclusivo hasta tacones de alta costura, pensados para quienes exigen excelencia y sofisticación en cada paso. Nuestra pasión es redefinir el estándar de la moda en Venezuela, ofreciendo piezas únicas que elevan tu estilo personal. En VORA Elite, no solo adquieres un par de zapatos; inviertes en presencia, autoridad y un estándar inquebrantable de lujo minimalista y estética impecable. Visítanos en nuestro showroom y experimenta la verdadera exclusividad con asesoría personalizada."
        },
        "openInfo": {
            "status": "CLOSED_TEMPORARILY" # Evita bloqueos hasta inauguración
        }
    }

    try:
        # Creación de la ubicación
        print(f"Desplegando location en la cuenta {account_name}...")
        request = service.accounts().locations().create(parent=account_name, body=location_data)
        response = request.execute()
        print("¡Despliegue exitoso!")
        print(f"Location Name: {response.get('name')}")
    except Exception as e:
        print(f"Error durante el despliegue del perfil: {e}")

if __name__ == '__main__':
    deploy_vora_profile()
