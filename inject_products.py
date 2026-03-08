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
  {"file": "PHOTO-2026-02-28-13-28-31.jpg", "category": "Heel", "name": "Navy Block", "desc": "Tacón alto grueso en azul marino de gamuza.", "price": "85.00", "sizes": ["37", "38", "39"]},
  {"file": "media__1772981760642.jpg", "category": "CAT", "name": "VORA x CAT Black Edition", "desc": "Zapatos todoterreno negros. Incluye Gorra Oficial y Llavero.", "price": "59.99", "sizes": ["38", "39", "40", "41", "42", "43", "44"]},
  {"file": "media__1772981760662.jpg", "category": "CAT", "name": "VORA x CAT Brown Rust", "desc": "Zapatos todoterreno marrones. Incluye Gorra Oficial y Llavero.", "price": "59.99", "sizes": ["38", "39", "40", "41", "42", "43", "44"]},
  {"file": "media__1772981760756.jpg", "category": "CAT", "name": "VORA x CAT Sand Desert", "desc": "Zapatos todoterreno arena/negro. Incluye Gorra Oficial y Llavero.", "price": "59.99", "sizes": ["38", "39", "40", "41", "42", "43", "44"]},
  {"file": "media__1772981760766.jpg", "category": "CAT", "name": "VORA x CAT True Honey", "desc": "Zapatos de trabajo color miel. Incluye Gorra Oficial y Llavero.", "price": "59.99", "sizes": ["38", "39", "40", "41", "42", "43", "44"]}
]

sneakers_html = ""
heels_html = ""
cat_html = ""

def build_card(prod, index, is_hidden=False, category_type="sneaker"):
    src = os.path.join(inventory_dir, prod["file"])
    ext = os.path.splitext(prod["file"])[1]
    
    slug = prod["name"].lower().replace(' ', '-')
    safe_name = f"{slug}{ext}"
    
    # Sub-categorization logic for filters
    name_lower = prod['name'].lower()
    sub_category = "todos"
    
    if prod['category'] == 'Sneaker':
        if "onyx" in name_lower or "shadow" in name_lower or "midnight" in name_lower or "core" in name_lower:
            sub_category = "monocromo"
        elif "runner" in name_lower or "air" in name_lower or "chrome" in name_lower or "trainer" in name_lower:
            sub_category = "retro"
        else:
            sub_category = "tech"
    else: # Heel
        if "pump" in name_lower or "classic" in name_lower or "slingback" in name_lower:
            sub_category = "classic"
        elif "sandal" in name_lower or "pattern" in name_lower:
            sub_category = "noche"
        else:
            sub_category = "block"
    
    dst = os.path.join(assets_dir, safe_name)
    shutil.copy2(src, dst)
    
    img_url = f"./assets/images/products/{safe_name}?v=1.0"
    
    # We will pass the available sizes as a comma-separated string to the modal
    sizes_str = ",".join(prod["sizes"])

    hidden_class = f"hidden extra-{category_type}" if is_hidden else ""

    return f"""
    <!-- Product Card {index} -->
    <div class="group flex flex-col bg-white border border-transparent hover:border-gray-200 transition-colors {hidden_class}" data-category="{sub_category}">
        <div class="relative aspect-square overflow-hidden mb-4 premium-hover flex items-center justify-center p-4">
            <img src="{img_url}" alt="{prod['name']}" class="object-cover w-full h-full mix-blend-darken hover:mix-blend-normal scale-110 object-center">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/5 transition-colors duration-300 pointer-events-none"></div>
        </div>
        <div class="flex-grow flex flex-col p-4 pt-0">
            <h3 class="font-display text-xl font-bold uppercase tracking-tight mb-1 text-black">{prod['name']}</h3>
            <p class="text-gray-500 text-sm mb-4 line-clamp-2">{prod['desc']}</p>

            <div class="mt-auto flex flex-col pt-4 gap-2 border-t border-gray-100">
                <span class="text-xs text-gray-500 uppercase tracking-widest font-semibold mb-[-8px]">Lujo de Élite, Precio Real</span>
                <div class="flex items-center gap-3 w-full mb-1 mt-1">
                    <span class="font-display font-black text-2xl tracking-tight text-black">${prod['price']}</span>
                    <del class="text-sm text-gray-400 font-medium">$120.00</del>
                </div>
                <div class="flex items-center gap-2 w-full">
                    <button onclick="openQuickView('{prod['name']}', '{prod['price']}', '{img_url}', '{sizes_str}', 'prod-{index}')" class="flex-[1] bg-white text-black border border-black hover:bg-black hover:text-white uppercase text-xs font-bold tracking-widest px-1 py-3 transition-colors flex items-center justify-center gap-1 group/btn">
                        <i class="ph ph-bag text-lg group-hover/btn:scale-110 transition-transform"></i>
                    </button>
                    <button onclick="openQuickView('{prod['name']}', '{prod['price']}', '{img_url}', '{sizes_str}', 'prod-{index}')" class="flex-[2] bg-black text-white hover:bg-gray-800 border border-black uppercase text-xs font-bold tracking-widest px-2 py-3 transition-colors flex items-center justify-center gap-2 group/qv">
                        <span>Ver Detalles</span>
                        <i class="ph-bold ph-arrow-right text-lg group-hover/qv:translate-x-1 transition-transform"></i>
                    </button>
                </div>
                <!-- Payment Badges -->
                <div class="flex items-center justify-center gap-3 mt-3 text-[10px] text-gray-400 font-medium uppercase tracking-wider">
                    <span class="flex items-center gap-1"><i class="ph ph-wallet"></i> Zelle</span>
                    <span class="flex items-center gap-1"><i class="ph ph-currency-btc"></i> USDT</span>
                    <span class="flex items-center gap-1"><i class="ph ph-credit-card"></i> Cuotas</span>
                </div>
            </div>
        </div>
    </div>
    """

def build_cat_card(prod, index):
    src = os.path.join(inventory_dir, prod["file"])
    dst = os.path.join(assets_dir, prod["file"])
    shutil.copy2(src, dst)
    img_url = f"./assets/images/products/{prod['file']}?v=1.0"
    sizes_str = ",".join(prod["sizes"])

    return f"""
    <!-- Product Card {index} -->
    <div class="group flex flex-col bg-white border border-gray-200 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 relative">
        <!-- Badge -->
        <div class="absolute top-4 left-4 z-10 bg-[#FFCC00] text-black font-black text-xs uppercase tracking-widest px-3 py-1 shadow-md">
            🎁 COMBO INCLUIDO
        </div>
        
        <div class="relative aspect-[4/3] overflow-hidden mb-0 bg-gray-100 flex items-center justify-center p-0">
            <img src="{img_url}" alt="{prod['name']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
        </div>
        <div class="flex-grow flex flex-col p-5 bg-white">
            <h3 class="font-display text-xl sm:text-2xl font-black uppercase tracking-tight mb-2 text-black leading-tight">{prod['name']}</h3>
            <p class="text-gray-600 text-sm mb-4 line-clamp-2 leading-relaxed">{prod['desc']}</p>

            <div class="mt-auto flex flex-col gap-3">
                <div class="bg-gray-50 p-3 rounded-sm border border-gray-100 flex items-center gap-3">
                    <i class="ph-fill ph-gift text-2xl text-[#FFCC00]"></i>
                    <div class="text-xs font-bold text-gray-800 leading-tight">Gorra Oficial + Llavero CAT<br><span class="text-[10px] text-gray-500 font-normal uppercase">Ambos incluídos en el precio</span></div>
                </div>

                <div class="flex items-end justify-between w-full mt-2">
                    <div>
                        <del class="text-sm text-gray-400 font-bold">$110.00</del>
                        <div class="font-display font-black text-3xl tracking-tight text-black">${prod['price']}</div>
                    </div>
                </div>
                
                <div class="flex items-center gap-2 w-full mt-2">
                    <button onclick="openQuickView('{prod['name']}', '{prod['price']}', '{img_url}', '{sizes_str}', 'prod-{index}')" class="flex-[1] bg-black text-white hover:bg-[#FFCC00] hover:text-black hover:border-black border-2 border-black uppercase text-xs font-black tracking-widest px-2 py-4 transition-colors flex items-center justify-center gap-2 group/qv">
                        <span>Llevar Oferta 3x1</span>
                        <i class="ph-bold ph-shopping-cart text-lg"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>
    """

sneakers_count = 0
heels_count = 0

idx = 100 # start index to avoid collision with cart dummy code if any
for prod in products_data:
    idx += 1
    if prod["category"] == "Sneaker":
        sneakers_count += 1
        is_hidden = True if sneakers_count > 6 else False
        sneakers_html += build_card(prod, idx, is_hidden, "sneaker")
    elif prod["category"] == "Heel":
        heels_count += 1
        is_hidden = True if heels_count > 6 else False
        heels_html += build_card(prod, idx, is_hidden, "heel")
    elif prod["category"] == "CAT":
        cat_html += build_cat_card(prod, idx)

# Add 'Ver mas' buttons to the grids
sneakers_html += """
</div>
<div class="w-full flex justify-center mt-12 items-center" id="btn-more-sneakers">
    <button onclick="document.querySelectorAll('.extra-sneaker').forEach(el => el.classList.remove('hidden')); this.parentElement.style.display='none';" class="bg-black text-white hover:bg-gray-800 border-2 border-black uppercase text-sm font-black tracking-widest px-10 py-4 transition-colors">
        Ver Más Modelos
    </button>
</div>
<!-- Closing div that original regex expects -->
<div>"""

heels_html += """
</div>
<div class="w-full flex justify-center mt-12 items-center" id="btn-more-heels">
    <button onclick="document.querySelectorAll('.extra-heel').forEach(el => el.classList.remove('hidden')); this.parentElement.style.display='none';" class="bg-black text-white hover:bg-gray-800 border-2 border-black uppercase text-sm font-black tracking-widest px-10 py-4 transition-colors">
        Ver Más Modelos
    </button>
</div>
<!-- Closing div that original regex expects -->
<div>"""

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Sneakers Grid
sneakers_pattern = r'(<!-- CATEGORY 1: SNEAKERS URBAN ELITE -->.*?<div class="grid [^"]+">).*?(</div>\s*</div>\s*</section>)'
# We adjust the replacement to account for the extra divs we added in sneakers_html
content = re.sub(sneakers_pattern, r'\g<1>\n' + sneakers_html + r'\n</div>\n</section>', content, flags=re.DOTALL)

# Replace Heels Grid
heels_pattern = r'(<!-- CATEGORY 2: GALA & HEELS COLLECTION -->.*?<div class="grid [^"]+">).*?(</div>\s*</div>\s*</section>)'
content = re.sub(heels_pattern, r'\g<1>\n' + heels_html + r'\n</div>\n</section>', content, flags=re.DOTALL)

# Replace CAT Grid
cat_pattern = r'(<!-- CATEGORY 3: URBAN WORKWEAR & CASUAL -->.*?<div class="grid [^"]+">).*?(</div>\s*</div>\s*</section>)'
# CAT doesn't have extra divs, so we restore its standard closing tag closure
content = re.sub(cat_pattern, r'\g<1>\n' + cat_html + r'\n</div>\n</div>\n</section>', content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Injected all 21 products successfully!")
