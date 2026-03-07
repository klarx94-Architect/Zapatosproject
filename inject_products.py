import os
import shutil
import re

inventory_dir = r"C:\Users\Alex Rosales\.gemini\antigravity\scratch\Zapatosproject\inventory"
assets_dir = r"C:\Users\Alex Rosales\.gemini\antigravity\scratch\Zapatosproject\web\assets\images\products"
html_path = r"C:\Users\Alex Rosales\.gemini\antigravity\scratch\Zapatosproject\web\index.html"

os.makedirs(assets_dir, exist_ok=True)

# Categorized data from AI agent
products_data = [
  {"file": "PHOTO-2026-02-28-13-29-37.jpg", "category": "Sneaker", "name": "Rose Runner", "desc": "Aceleración estética con detalles magenta. Construcción premium.", "price": "85.00", "sizes": ["38", "39", "40"]},
  {"file": "PHOTO-2026-02-28-13-31-01(1).jpg", "category": "Sneaker", "name": "Onyx Street", "desc": "Diseño clásico en blanco y negro. Lujo callejero.", "price": "85.00", "sizes": ["41", "42", "43"]},
  {"file": "PHOTO-2026-02-28-13-31-01.jpg", "category": "Sneaker", "name": "Titan Sand", "desc": "Construcción táctica beige y negro. Versatilidad suprema.", "price": "85.00", "sizes": ["40", "41", "42"]},
  {"file": "PHOTO-2026-02-28-13-29-37(1).jpg", "category": "Sneaker", "name": "Blush Trainer", "desc": "Estructura rosa con acentos oscuros. Equilibrio cromático perfecto.", "price": "85.00", "sizes": ["37", "38", "39"]},
  {"file": "PHOTO-2026-02-28-13-29-36(1).jpg", "category": "Sneaker", "name": "Shadow Flex", "desc": "Negro absoluto. Perfil bajo y silueta dominante.", "price": "85.00", "sizes": ["39", "40", "41"]},
  {"file": "PHOTO-2026-02-28-13-29-36.jpg", "category": "Sneaker", "name": "Arctic Cloud", "desc": "Corte de diseño chunky en blanco puro. Amortiguación máxima.", "price": "85.00", "sizes": ["40", "41", "42"]},
  {"file": "PHOTO-2026-02-28-13-29-37(2).jpg", "category": "Sneaker", "name": "Midnight Core", "desc": "Diseño robusto oscuro con franjas de contraste.", "price": "85.00", "sizes": ["39", "40", "41", "42"]},
  {"file": "PHOTO-2026-02-28-13-31-34.jpg", "category": "Sneaker", "name": "Obsidian Air", "desc": "Cápsula de aire visible. Presencia innegable en el asfalto.", "price": "85.00", "sizes": ["39", "40", "41"]},
  {"file": "PHOTO-2026-02-28-13-32-20.jpg", "category": "Sneaker", "name": "Carbon Max", "desc": "Sistema Elite con cámara translúcida y texturas mixtas.", "price": "85.00", "sizes": ["40", "41", "42"]},
  {"file": "PHOTO-2026-02-28-13-33-51.jpg", "category": "Sneaker", "name": "Silver Chrome", "desc": "Capas reflectantes en blanco y cromo. Ingeniería de punta.", "price": "85.00", "sizes": ["37", "38", "39"]},
  {"file": "PHOTO-2026-02-28-13-23-05(1).jpg", "category": "Heel", "name": "Crimson Pump", "desc": "Stiletto rojo clásico. Altura y elegancia innegociable.", "price": "85.00", "sizes": ["36", "37", "38"]},
  {"file": "PHOTO-2026-02-28-13-23-05.jpg", "category": "Heel", "name": "Noir Pump", "desc": "Básico indispensable. Corte fino color negro.", "price": "85.00", "sizes": ["37", "38", "39"]},
  {"file": "PHOTO-2026-02-28-13-24-42(1).jpg", "category": "Heel", "name": "Noir Sandal", "desc": "Tiras de noche oscuras. Diseño fino y delicado.", "price": "85.00", "sizes": ["36", "37", "38"]},
  {"file": "PHOTO-2026-02-28-13-24-42.jpg", "category": "Heel", "name": "Ruby Sandal", "desc": "Sandalia roja de tacón alto. Estructura de poder visual.", "price": "85.00", "sizes": ["37", "38", "39"]},
  {"file": "PHOTO-2026-02-28-13-25-28(1).jpg", "category": "Heel", "name": "Noir Block", "desc": "Tacón cuadrado negro cerrado. Comodidad simétrica.", "price": "85.00", "sizes": ["36", "37", "38"]},
  {"file": "PHOTO-2026-02-28-13-25-28.jpg", "category": "Heel", "name": "Nude Classic", "desc": "Zapatilla plana tono beige. Suavidad y confort premium.", "price": "85.00", "sizes": ["36", "37", "38"]},
  {"file": "PHOTO-2026-02-28-13-26-24.jpg", "category": "Heel", "name": "Noir Slingback", "desc": "Zapato punta fina con talón descubierto. Silueta afilada.", "price": "85.00", "sizes": ["37", "38", "39"]},
  {"file": "PHOTO-2026-02-28-13-26-25.jpg", "category": "Heel", "name": "Ruby Pattern", "desc": "Diseño híbrido plano con patrón rojo destalonado.", "price": "85.00", "sizes": ["37", "38", "39"]},
  {"file": "PHOTO-2026-02-28-13-27-33.jpg", "category": "Heel", "name": "Cognac Block", "desc": "Sandalia de tacón grueso tono arena/bronce.", "price": "85.00", "sizes": ["37", "38", "39"]},
  {"file": "PHOTO-2026-02-28-13-27-34.jpg", "category": "Heel", "name": "Onyx Block", "desc": "Sandalia plataforma de correas negras gruesas.", "price": "85.00", "sizes": ["36", "37", "38"]},
  {"file": "PHOTO-2026-02-28-13-28-31.jpg", "category": "Heel", "name": "Navy Block", "desc": "Tacón alto grueso en azul marino de gamuza.", "price": "85.00", "sizes": ["37", "38", "39"]}
]

sneakers_html = ""
heels_html = ""

def build_card(prod, index):
    src = os.path.join(inventory_dir, prod["file"])
    ext = os.path.splitext(prod["file"])[1]
    
    slug = prod["name"].lower().replace(' ', '-')
    safe_name = f"{slug}{ext}"
    
    dst = os.path.join(assets_dir, safe_name)
    shutil.copy2(src, dst)
    
    img_url = f"./assets/images/products/{safe_name}?v=1.0"
    
    options = "".join([f'<option value="{size}">{size}</option>' for size in range(35, 46)])
    sizes_html = f"""<select id="size-input-prod-{index}" class="w-full bg-gray-50 border border-gray-200 text-center text-sm font-bold focus:outline-none focus:border-black transition-colors py-1 px-2 cursor-pointer"><option value="" disabled selected>Talla...</option>{options}</select>"""
        
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
                <span class="text-xs text-gray-500 uppercase tracking-widest font-semibold mb-[-8px]">Lujo de Élite, Precio Real</span>
                <div class="flex items-center gap-3 w-full mb-1 mt-1">
                    <span class="font-display font-black text-2xl tracking-tight text-black">${prod['price']}</span>
                    <del class="text-sm text-gray-400 font-medium">$120.00</del>
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
