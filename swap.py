html_path = r"C:\Users\Alex Rosales\.gemini\antigravity\scratch\Zapatosproject\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix social proof text "Alguien en "
content = content.replace(
    '''<p class="text-xs font-bold text-black leading-tight">Alguien en <span id="sp-location" class="text-[#FF3333]">Caracas</span> compró</p>''',
    '''<p class="text-xs font-bold text-black leading-tight"><span id="sp-location" class="text-[#FF3333]">Caracas</span> compró</p>'''
)

cat_pattern = r'(<!-- CATEGORY 3: URBAN WORKWEAR & CASUAL -->.*?</section>\n)'
sneakers_pattern = r'(<!-- CATEGORY 1: SNEAKERS URBAN ELITE -->.*?</section>\n)'

cat_match = re.search(cat_pattern, content, re.DOTALL)
sneakers_match = re.search(sneakers_pattern, content, re.DOTALL)

if cat_match and sneakers_match:
    cat_html = cat_match.group(1)
    sneakers_html = sneakers_match.group(1)

    content = content.replace(cat_html, "")
    content = content.replace(sneakers_html, "")
    
    scarcity_pattern = r'(<!-- SCARCITY BANNER -->.*?</div>\n        </div>\n)'
    scarcity_match = re.search(scarcity_pattern, content, re.DOTALL)
    
    if scarcity_match:
        scarcity_html = scarcity_match.group(1)
        new_content = content.replace(scarcity_html, scarcity_html + "\n        " + cat_html + "\n        " + sneakers_html)
        
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully reordered sections and fixed social proof.")
    else:
        print("Scarcity section not found!")
else:
    print("Could not find sections!")
