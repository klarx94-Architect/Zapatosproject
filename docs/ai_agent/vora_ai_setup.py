import os
import google.generativeai as genai
from dotenv import load_dotenv

# Dependencias Flask simuladas para entorno omnicanal
from flask import Flask, request, jsonify

app = Flask(__name__)
load_dotenv()

# --- GEMINI SETUP ---
api_key = os.getenv("GEMINI_API_KEY")
if api_key and api_key != "tu_api_key_aqui":
    genai.configure(api_key=api_key)
else:
    print("Advertencia: GEMINI_API_KEY no configurada en .env.")

prompt_path = os.path.join(os.path.dirname(__file__), 'system_prompt_vora_ai.md')
system_instruction = ""
try:
    with open(prompt_path, 'r', encoding='utf-8') as f:
        system_instruction = f.read()
except FileNotFoundError:
    print(f"Error: No se encontró el System Prompt en {prompt_path}")

try:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=system_instruction,
        generation_config={"temperature": 0.4, "max_output_tokens": 800}
    )
except Exception as e:
    model = None

# --- WEBHOOK ENDPOINTS (META OMNICHANNEL) ---
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "vora_elite_secure_token")

@app.route("/webhook", methods=["GET"])
def verify_webhook():
    """Verificación OAUTH requerida por Meta API (Instagram & WhatsApp)"""
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("Webhook verificado exitosamente por Meta.")
            return challenge, 200
        else:
            return "Forbidden", 403
    return "OK", 200

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    """Recepción de Mensajes Omnicanal (WhatsApp y DMs de Instagram)"""
    data = request.json
    
    if data.get("object") in ["whatsapp_business_account", "instagram"]:
        for entry in data.get("entry", []):
            for messaging_event in entry.get("messaging", []): # Formato IG
                sender_id = messaging_event["sender"]["id"]
                message_text = messaging_event.get("message", {}).get("text", "")
                
                print(f"[INSTAGRAM] Mensaje recibido de {sender_id}: {message_text}")
                # Aquí inyectaríamos el modelo de Gemini: model.generate_content(...)
                
            for changes in entry.get("changes", []): # Formato WA
                value = changes.get("value", {})
                if "messages" in value:
                    for msg in value["messages"]:
                        sender_phone = msg["from"]
                        msg_text = msg.get("text", {}).get("body", "")
                        
                        print(f"[WHATSAPP {sender_phone}] Mensaje: {msg_text}")
                        # Respuesta de Gemini aquí.
                        
        return jsonify({"status": "ok"}), 200
    return "Not Found", 404

if __name__ == "__main__":
    print("VORA Concierge AI - Servidor Omnicanal (IG & WA) Inicializado.")
    # app.run(port=5000) # Comentado para no bloquear el hilo de bash en pruebas locales.
