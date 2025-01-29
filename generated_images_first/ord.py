import os
import re

# Ottieni la lista dei file ordinata numericamente
file_list = sorted(os.listdir(), key=lambda x: int(re.search(r'image_(\d+)', x).group(1)) if re.search(r'image_(\d+)', x) else float('inf'))

# Loop per rinominare i file nel formato "image_XXX.png"
for file in file_list:
    match = re.match(r'image_(\d+)', file)  # Cerca la parte "image_X"
    if match:
        num = int(match.group(1))  # Estrai il numero
        ext = os.path.splitext(file)[1]  # Estrai l'estensione (.png, .jpg, ecc.)
        new_name = f"image_{num:03d}{ext}"  # Nuovo nome con z-fill a 3 cifre
        
        if file != new_name:  # Evita di rinominare se il nome è già corretto
            os.rename(file, new_name)
            print(f"✅ Rinominato: {file} -> {new_name}")
