# VORA Elite: Flujo Lógico de Cierre de Ventas (WhatsApp)

Este diagrama representa los estados por los que el *VORA Concierge* debe guiar al cliente hasta convertir la venta.

```mermaid
graph TD
    A[1. Saludo Inicial] --> B[2. Calificación del Cliente]
    B --> C{¿Qué busca?}
    C -->|Sneakers Urbanos| D[3A. Presentación: Apex Obsidian o Zenith White]
    C -->|Gala / Femenino| E[3B. Presentación: Stardust Chrome]
    C -->|Solo curiosidad/Precio| F[3C. Generación de Valor & Escasez]
    
    D --> G[4. Manejo de Objeciones]
    E --> G
    F --> G
    
    G --> H{Objeción Principal}
    H -->|Talla| I[Tabla de Medidas en CM]
    H -->|Precio| J[Anclaje: Valor Real 130$ vs VORA 85$]
    H -->|Envío / Confianza| K[Garantía: Envío Gratis Asegurado desde Táchira]
    
    I --> L[5. Intención de Compra Confirmada]
    J --> L
    K --> L
    
    L --> M[6. Captura de Datos de Envío]
    M --> N[Nombre, Cédula, Teléfono, Estado, Dirección/Agencia]
    
    N --> O[7. Cierre Financiero]
    O --> P[Selección de Pago: Binance / Zelle / Pago Móvil]
    P --> Q[8. Confirmación de Recepción y Felicidades]
```

## Leyenda de Fases para el LLM (Gestión de Estado)
1. **Saludo:** Establecer marco de autoridad y elegancia.
2. **Calificación:** Preguntar sutilmente si busca calzado para diario, evento especial, etc.
3. **Presentación:** Enviar imágenes del catálogo ganador en `/inventory` y soltar el Copy SEO adaptado.
4. **Objeciones:** Aplicar directivas del System Prompt relativas a tallas y confianza.
5. **Cierre:** Hacer la pregunta afirmativa ("¿A qué nombre reservamos su par exclusivo?").
6. **Datos:** Solicitar formato estándar de envíos en Venezuela (MRW/Zoom/Tealca).
7. **Finanzas:** Proveer los datos bancarios exactos solo cuando los datos de envío estén completos.
