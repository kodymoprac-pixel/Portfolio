import os
import json

images_dir = "images"
output_file = "gallery_list.js"

gallery = {}

# projde všechny podsložky
for folder in os.listdir(images_dir):
    folder_path = os.path.join(images_dir, folder)
    if os.path.isdir(folder_path):
        files = [f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif"))]
        if files:
            # relativní cesty, aby fungovalo na GitHub Pages
            gallery[folder] = [f"{images_dir}/{folder}/{f}" for f in files]

# vytvoří gallery_list.js
with open(output_file, "w", encoding="utf-8") as f:
    f.write("const images = " + json.dumps(gallery, indent=2) + ";")

print(f"✅ Soubor {output_file} vygenerován s {len(gallery)} sekcemi.")

