import os
import shutil
import re

inventory_dir = r"C:\Users\Alex Rosales\.gemini\antigravity\scratch\Zapatosproject\inventory"
assets_dir = r"C:\Users\Alex Rosales\.gemini\antigravity\scratch\Zapatosproject\web\assets\images\products"
html_path = r"C:\Users\Alex Rosales\.gemini\antigravity\scratch\Zapatosproject\web\index.html"

os.makedirs(assets_dir, exist_ok=True)

# Categorized data from AI agent
products_data = [
  {"file": "PHOTO-2026-02-28-13-23-05(1).jpg", "category": "Heel", "name": "VORA Stiletto Noir", "desc": "Corte infalible. Altura innegociable.", "price": "85.00", "sizes": ["36", "37", "38"]},
  {"file": "PHOTO-2026-02-28-13-23-05.jpg", "category": "Heel", "name": "VORA Velvet Night", "desc": "Suavidad nocturna. Elegancia absoluta.", "price": "85.00", "sizes": ["37", "38", "39"]},
  {"file": "PHOTO-2026-02-28-13-24-42(1).jpg", "category": "Heel", "name": "VORA Stardust Chrome", "desc": "Brillo espectacular. Diseño arquitectónico.", "price": "85.00", "sizes": ["36", "37", "38", "39"]},
  {"file": "PHOTO-2026-02-28-13-24-42.jpg", "category": "Heel", "name": "VORA Lumina Platin", "desc": "Elevación máxima. Estructura de poder.", "price": "85.00", "sizes": ["38", "39", "40"]},
  {"file": "PHOTO-2026-02-28-13-25-28(1).jpg", "category": "Sneaker", "name": "VORA Zenith White", "desc": "Blanco puro. Líneas aerodinámicas perfectas.", "price": "85.00", "sizes": ["40", "41", "42"]},
  {"file": "PHOTO-2026-02-28-13-25-28.jpg", "category": "Sneaker", "name": "VORA Aurora Blush", "desc": "Tonalidades suaves, desempeño urbano premium.", "price": "85.00", "sizes": ["36", "37", "38"]},
  {"file": "PHOTO-2026-02-28-13-26-24.jpg", "category": "Sneaker", "name": "VORA Crimson Flare", "desc": "Rojo intenso. Presencia innegable en el asfalto.", "price": "85.00", "sizes": ["39", "40", "41"]},
  {"file": "PHOTO-2026-02-28-13-26-25.jpg", "category": "Sneaker", "name": "VORA Chroma Shift", "desc": "Diseño híbrido. Comodidad que redefine tendencias.", "price": "85.00", "sizes": ["37", "38", "39"]},
  {"file": "PHOTO-2026-02-28-13-27-33.jpg", "category": "Sneaker", "name": "VORA Apex Obsidian", "desc": "Negro absoluto. Silueta dominante y furtiva.", "price": "85.00", "sizes": ["40", "41", "42", "43"]},
  {"file": "PHOTO-2026-02-28-13-27-34.jpg", "category": "Sneaker", "name": "VORA Velocity Neon", "desc": "Ligereza extrema. Detalles vibrantes.", "price": "85.00", "sizes": ["41", "42", "43"]},
  {"file": "PHOTO-2026-02-28-13-28-31.jpg", "category": "Sneaker", "name": "VORA Ivory Step", "desc": "Clásico reimaginado. Puntos de confort estratégico.", "price": "85.00", "sizes": ["39", "40", "41"]},
  {"file": "PHOTO-2026-02-28-13-29-36(1).jpg", "category": "Sneaker", "name": "VORA Nova Red", "desc": "Edición limitada. Estructura de impacto.", "price": "85.00", "sizes": ["38", "39", "40"]},
  {"file": "PHOTO-2026-02-28-13-29-36.jpg", "category": "Sneaker", "name": "VORA Horizon Blue", "desc": "Innovación táctica. Desgarro visual deportivo.", "price": "85.00", "sizes": ["40", "41", "42"]},
  {"file": "PHOTO-2026-02-28-13-29-37(1).jpg", "category": "Sneaker", "name": "VORA Titan Sand", "desc": "Tonos tierra orgánicos. Versatilidad suprema.", "price": "85.00", "sizes": ["42", "43", "44"]},
  {"file": "PHOTO-2026-02-28-13-29-37(2).jpg", "category": "Sneaker", "name": "VORA Matrix Black", "desc": "Sistema de amortiguación Elite. Oscuro e imponente.", "price": "85.00", "sizes": ["39", "40", "41", "42"]},
  {"file": "PHOTO-2026-02-28-13-29-37.jpg", "category": "Sneaker", "name": "VORA Phantom Runner", "desc": "Aceleración estética. Construcción de malla premium.", "price": "85.00", "sizes": ["38", "39", "40"]},
  {"file": "PHOTO-2026-02-28-13-31-01(1).jpg", "category": "Sneaker", "name": "VORA Onyx Classic", "desc": "Detalle inmaculado. El estándar del lujo callejero.", "price": "85.00", "sizes": ["41", "42", "43"]},
  {"file": "PHOTO-2026-02-28-13-31-01.jpg", "category": "Sneaker", "name": "VORA Quantum Grey", "desc": "Texturas mixtas. Equilibrio cromático perfecto.", "price": "85.00", "sizes": ["40", "41", "42"]},
  {"file": "PHOTO-2026-02-28-13-31-34.jpg", "category": "Sneaker", "name": "VORA Solar Orange", "desc": "Explosión visual. Sello de identidad VORA.", "price": "85.00", "sizes": ["39", "40", "41"]},
  {"file": "PHOTO-2026-02-28-13-32-20.jpg", "category": "Sneaker", "name": "VORA Celeste Pearl", "desc": "Corte preciso. Detalles reflectantes exclusivos.", "price": "85.00", "sizes": ["37", "38", "39"]},
  {"file": "PHOTO-2026-02-28-13-33-51.jpg", "category": "Sneaker", "name": "VORA Prism Light", "desc": "Transiciones tonales. Ingeniería de punta.", "price": "85.00", "sizes": ["41", "42", "43"]}
]

sneakers_html = ""
heels_html = ""

def build_card(prod, index):
    src = os.path.join(inventory_dir, prod["file"])
    ext = os.path.splitext(prod["file"])[1]
    safe_name = f"product-{index}{ext}"
    dst = os.path.join(assets_dir, safe_name)
    shutil.copy2(src, dst)
    
    img_url = f"./assets/images/products/{safe_name}"
    
    sizes_html = ""
    for idx, s in enumerate(prod['sizes']):
        active = ' active' if idx == 1 else ''
        sizes_html += f"""<button onclick="selectSize(this, 'prod-{index}')" class="size-btn w-8 h-8 flex items-center justify-center border border-gray-200 text-sm transition-colors hover:border-black{active}">{s}</button>"""
        
    return f"""
    <!-- Product Card {index} -->
    <div class="group flex flex-col bg-white border border-transparent hover:border-gray-200 transition-colors">
        <div class="relative aspect-square overflow-hidden mb-4 premium-hover flex items-center justify-center p-4">
            <img src="{img_url}" alt="{prod['name']}" class="object-cover w-full h-full mix-blend-darken hover:mix-blend-normal scale-110 object-center">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/5 transition-colors duration-300 pointer-events-none"></div>
        </div>
        <div class="flex-grow flex flex-col p-4 pt-0">
            <h3 class="font-display text-xl font-bold uppercase tracking-tight mb-1 text-black">{prod['name']}</h3>
            <p class="text-gray-500 text-sm mb-4 line-clamp-2">{prod['desc']}</p>

            <div class="flex items-center space-x-2 mb-4 mt-auto">
                <span class="bg-gray-100 text-black text-xs px-2 py-1 uppercase tracking-wider font-semibold">Tallas</span>
                <div class="flex gap-2" id="sizes-prod-{index}">
                    {sizes_html}
                </div>
            </div>

            <div class="mt-auto flex flex-col pt-4 gap-2 border-t border-gray-100">
                <div class="flex justify-between items-center w-full mb-1 mt-1">
                    <span class="font-display font-medium text-2xl tracking-tight">${prod['price']}</span>
                </div>
                <div class="flex gap-2 w-full">
                    <button onclick="addToCart('{prod['name']}', {prod['price']}, 'prod-{index}', '{img_url}')" class="flex-[1] bg-white text-black border border-black hover:bg-black hover:text-white uppercase text-xs font-bold tracking-widest px-1 py-3 transition-colors flex items-center justify-center gap-1 group/btn">
                        <i class="ph ph-bag text-lg group-hover/btn:scale-110 transition-transform"></i>
                    </button>
                    <button onclick="checkoutSingleItem('{prod['name']}', 'prod-{index}')" class="flex-[2] bg-black text-white hover:bg-[#25D366] border border-black uppercase text-xs font-bold tracking-widest px-2 py-3 transition-colors flex items-center justify-center gap-2 group/wp">
                        <span>Pedir</span>
                        <i class="ph-fill ph-whatsapp-logo text-lg group-hover/wp:scale-110 transition-transform"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>
    """

idx = 100 # start index to avoid collision with cart dummy code if any
for prod in products_data:
    idx += 1
    card = build_card(prod, idx)
    if prod["category"] == "Sneaker":
        sneakers_html += card
    else:
        heels_html += card

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Sneakers Grid
sneakers_pattern = r'(<!-- CATEGORY 1: SNEAKERS URBAN ELITE -->.*?<div class="grid [^"]+">).*?(</div>\s*</div>\s*</section>)'
content = re.sub(sneakers_pattern, r'\g<1>\n' + sneakers_html + r'\n\g<2>', content, flags=re.DOTALL)

# Replace Heels Grid
heels_pattern = r'(<!-- CATEGORY 2: GALA & HEELS COLLECTION -->.*?<div class="grid [^"]+">).*?(</div>\s*</div>\s*</section>)'
content = re.sub(heels_pattern, r'\g<1>\n' + heels_html + r'\n\g<2>', content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Injected all 21 products successfully!")
