# Integración de Catálogo VORA con Meta Commerce API

Para lograr una sincronización automática en tiempo real entre nuestro archivo `catalog_strategy.md` (o una futura base de datos) y el catálogo visible en WhatsApp Business / Instagram Shopping, necesitamos configurar un **flujo Server-to-Server** a través de la Meta Graph API.

## 1. Requisitos de Identificación (Business Manager)
Para que Antigravity pueda inyectar los productos al ecosistema corporativo, necesitamos que el Líder Estratégico o el Usuario extraigan los siguientes datos del **Meta Business Suite**:

- **Business Manager ID (BM ID):** El identificador único del negocio (se encuentra en _Configuración del Negocio > Información del Negocio_).
- **Catalog ID:** El ID del catálogo vacío que crearemos en el Commerce Manager para que el script lo llene.
- **WhatsApp Business Account ID (WABA ID):** El ID de la cuenta de WhatsApp oficial (obligatorio para vincular el catálogo al chat).

## 2. Permisos y System User
Dado que operaremos mediante scripts autónomos, usar tu cuenta personal de Facebook no es escalable ni seguro. Necesitamos crear un **System User (Usuario del Sistema)**.

1. Navega a **Configuración del Negocio > Usuarios > Usuarios del sistema**.
2. Crea un usuario llamado "VORA AI Sync".
3. Asígnale el rol de **Empleado** o **Administrador** (recomendado para Commerce).
4. Genera un **Token de Acceso (Access Token)** permanente para este usuario.

**Permisos (Scopes) Obligatorios que el token debe tener:**
- `catalog_management` (Para añadir, modificar o borrar los Sneakers y Tacones).
- `whatsapp_business_messaging` (Para que el VORA Concierge pueda enviar fotos de los productos).
- `whatsapp_business_management` (Para configurar el perfil comercial).

## 3. Arquitectura del Flujo (Próxima Fase)
Una vez proveas el Token y los IDs, el sistema operará así:
1. El script local lee los modelos y precios.
2. Sube las imágenes de `inventory/` a un servidor de assets (o al propio GitHub Pages) ya que Meta exige URLs públicas para las imágenes.
3. Llama al endpoint `POST /{catalog_id}/products` de Graph API inyectando título, descripción SEO, precio de rebaja ($85) e imagen.
4. El catálogo de WhatsApp del número `+584163794800` se actualizará en segundos.
