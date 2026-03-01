import os
import google.generativeai as genai
from dotenv import load_dotenv

def setup_vora_ai():
    # 1. Cargar variables de entorno (asegurándose que exista el .env real)
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "tu_api_key_aqui":
        raise ValueError("Error: GEMINI_API_KEY no encontrada. Revisa el archivo .env.")

    # 2. Configurar el SDK
    genai.configure(api_key=api_key)
    
    # 3. Leer el alma del bot (System Prompt)
    prompt_path = os.path.join(os.path.dirname(__file__), 'system_prompt_vora_ai.md')
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            system_instruction = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: No se encontró el System Prompt en {prompt_path}")

    # 4. Inicializar el generador con el contexto del Concierge
    # Se recomienda gemini-1.5-flash para respuestas rápidas de chat
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=system_instruction,
        generation_config={
            "temperature": 0.4, # Baja temperatura para mantener el tono elegante y consistente
            "max_output_tokens": 800,
        }
    )
    
    print("VORA Concierge AI inicializado exitosamente.")
    return model

if __name__ == "__main__":
    # Test rápido
    try:
        agente = setup_vora_ai()
        chat = agente.start_chat()
        print("Bot listo para procesar WhatsApp webhooks.")
    except Exception as e:
        print(e)
