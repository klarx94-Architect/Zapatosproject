# Automatización de Mensajería: Instagram y WhatsApp Omnicanal

Para que el VORA Concierge (Gemini IA) pueda interceptar, leer y responder mensajes directamente en Instagram y WhatsApp, necesitamos configurar webhooks en Meta para Desarrolladores.

## 1. Requisitos Arquitectónicos de Meta (Lo que el Commander necesita proveer)
Para que mis scripts puedan comunicarse con Meta y editar perfiles (tanto IG como WA), no me sirven usuario y contraseña. Mi sistema funciona mediante APIs. **Esto es lo que requiero de tu panel de Meta Business Suite / Meta for Developers**:

1. **Meta Access Token (Token de Usuario de Sistema):** 
   - Necesitas crear una app en [Meta for Developers](https://developers.facebook.com/) de tipo "Negocios" (Business).
   - Este token será temporal o permanente (recomendado).
2. **Instagram Account ID (`IG_ACCOUNT_ID`):** El ID numérico de tu Instagram Profesional.
3. **WhatsApp Business Account ID (`WABA_ID`):** Para poder modificar el catálogo.
4. **WhatsApp Phone Number ID (`WHATSAPP_PHONE_ID`):** El ID de número de teléfono proporcionado por la API de WhatsApp, correspondiente al número +58 416-3794800.

## 2. Permisos y Entorno de Instagram
A tu token de Meta, deberás otorgarle estrictamente estos permisos (`scopes`):
- `instagram_manage_messages` (Para que el agente pueda responder DMs e historias).
- `pages_manage_metadata` (Para conectar la cuenta a automatización).
- `pages_read_engagement` y `pages_show_list` (Para leer comentarios y enlacar Páginas).

## 3. Fase de Configuración de Perfiles a Cargo de Antigravity
> *"En esta fase te encargarás de crear los perfiles y editarlos en fase básica, no subirás imágenes, descripciones o precios hasta que yo así te lo indique... Usarás el logotipo oscuro en negro monocromático."*

**Aclaración Técnica Importante sobre CREACIÓN de perfiles:**
Yo (tu IA) **no puedo** "crear un usuario/cuenta de Instagram nueva" desde cero vía código mediante la API de Meta. La arquitectura de seguridad de Instagram restringe la creación de cuentas a dispositivos móviles o flujos web manuales (para evitar bots). **De la misma forma**, en WhatsApp Business, el registro del número de teléfono en la Meta Cloud API requiere validación mediante código SMS o llamada. 

**Flujo correcto a realizar por el humano (Tú):**
1. Crea la cuenta básica de Instagram (con el nombre Vora Elite) desde la aplicación de Instagram en tu teléfono usando el logo negro monocromático.
2. Convierte ese Instagram en "Cuenta Profesional".
3. Vincula el Instagram a una "Página de Facebook" de la empresa.
4. Añade el número de WhatsApp (+58 416-3794800) a tu Business Manager y certifícalo con SMS.

**Lo que haré yo (IA Antigravity) una vez me des los IDs y el Token:**
- Aplicaré el script de configuración `deploy_whatsapp_profile.py` y uno similar para Instagram, inyectando los datos SEO, conectando el Webhook para la IA y estableciendo los mensajes de bienvenida.
- En futuras actualizaciones, mediante la directiva que dispongas, subiré programáticamente los 21 artículos, actualizaré descripciones y aplicaré ajustes finos de negocio, listos para tu revisión visual en la app real.
