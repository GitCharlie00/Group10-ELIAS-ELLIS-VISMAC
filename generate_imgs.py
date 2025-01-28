import os
from tqdm import tqdm
from diffusers import StableDiffusionPipeline
import torch

# Configurazione del percorso
file_path = "Unbiased_text_descriptions.txt"  # Percorso del file dei prompt
output_folder = "generated_images"  # Cartella per salvare le immagini

# Creazione della cartella di output
os.makedirs(output_folder, exist_ok=True)

# # Caricamento del modello
pipeline = StableDiffusionPipeline.from_pretrained("/stable-diffusion-xl-base-1.0")  # Modello migliore
pipeline = pipeline.to("cuda:0" if torch.cuda.is_available() else "cpu")

# Lettura dei prompt dal file
with open(file_path, "r", encoding="utf-8") as f:
    prompts = [line.strip() for line in f.readlines() if line.strip()]

# Generazione delle immagini con barra di progresso
for i, prompt in enumerate(tqdm(prompts, desc="Generazione delle immagini", unit="prompt")):
    try:
        # Genera l'immagine
        image = pipeline(prompt).images[0]

        # Salva l'immagine includendo il prompt nel nome del file
        sanitized_prompt = "_".join(prompt.split())[:100]  # Limita la lunghezza del nome del file a 100 caratteri
        output_path = os.path.join(output_folder, f"image_{i+1}_{sanitized_prompt}.png")
        image.save(output_path)
    except Exception as e:
        print(f"Errore durante la generazione dell'immagine per il prompt '{prompt}': {e}")