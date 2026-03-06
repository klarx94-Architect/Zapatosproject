import os
import glob
from PIL import Image

inventory_dir = r"C:\Users\Alex Rosales\.gemini\antigravity\scratch\Zapatosproject\inventory"
tmp_dir = r"C:\Users\Alex Rosales\.gemini\antigravity\scratch\Zapatosproject\tmp_thumbs"
os.makedirs(tmp_dir, exist_ok=True)

files = glob.glob(os.path.join(inventory_dir, "*.jpg")) + glob.glob(os.path.join(inventory_dir, "*.png"))

for f in files:
    try:
        with Image.open(f) as img:
            img.thumbnail((400, 400)) # Small enough for AI context, clear enough for categorization
            if img.mode != 'RGB':
                img = img.convert('RGB')
            basename = os.path.basename(f)
            out_path = os.path.join(tmp_dir, basename)
            img.save(out_path, format='JPEG', quality=70)
            print(f"Thumbnailed: {basename}")
    except Exception as e:
        print(f"Failed {f}: {e}")
