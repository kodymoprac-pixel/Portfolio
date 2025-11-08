import os
import json

# složka s obrázky
images_dir = "images"

# výstupní soubor
output_file = "gallery_list.js"

# slovník pro galerii
gallery = {}

# projdeme všechny podsložky v images_dir
for folder in os.listdir(images_dir):
    folder_path = os.path.join(images_dir, folder)
    if os.path.isdir(folder_path):
        # vezmeme jen obrázky
        files = [f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif"))]
        if files:
            # uložíme cestu k souboru relativní k webu
            gallery[folder] = [f"{images_dir}/{folder}/{f}" for f in files]

# vytvoříme gallery_list.js
with open(output_file, "w", encoding="utf-8") as f:
    f.write("const images = " + json.dumps(gallery, indent=2) + ";")

print(f"✅ Soubor {output_file} vygenerován s {len(gallery)} sekcemi.")

