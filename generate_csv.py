import os
import csv

# Percorsi delle cartelle delle immagini
# image_folders = [f"generated_images{i}" for i in range(15)]
image_folders = []
image_folders.insert(0, "/work/project/Group10-ELIAS-ELLIS-VISMAC/generated_images_first")

# Leggere i prompt dal file
prompt_file = "/work/project/Group10-ELIAS-ELLIS-VISMAC/Unbiased_text_descriptions.txt"
prompts = []

with open(prompt_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and ":" not in line:  # Filtra righe vuote e quelle con ':'
            prompts.append(line)

# Creare la struttura per il CSV
csv_data = []

def natural_sort_key(s):
    return [int(t) if t.isdigit() else t for t in s.split('_') if t]

for i, prompt in enumerate(prompts):
    row = [prompt]
    for folder in image_folders:
        folder_path = os.path.join(folder)
        image_files = sorted(os.listdir(folder_path), key=natural_sort_key)  # Ordina naturalmente
        if i < len(image_files):  # Assicurati che ci sia un'immagine alla posizione i
            image_path = os.path.join(folder, image_files[i])
            row.append(image_path)
        else:
            row.append("N/A")
    csv_data.append(row)

# Scrivere il file CSV
output_file = "/work/project/Group10-ELIAS-ELLIS-VISMAC/prompts_with_images.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Intestazione
    header = ["Prompt"] + image_folders
    writer.writerow(header)
    # Dati
    writer.writerows(csv_data)

print(f"File CSV generato: {output_file}")
