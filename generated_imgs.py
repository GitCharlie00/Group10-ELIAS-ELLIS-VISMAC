import os
import torch
from diffusers import FluxPipeline

file_path = "Unbiased_text_descriptions.txt"

pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16).to("cuda")

# Lettura prompts
with open(file_path, "r", encoding="utf-8") as f:
    prompts = [line.strip() for line in f.readlines() if line.strip()]

for j in range(15):
    output_folder = "generated_images" + str(j+100)
    os.makedirs(output_folder, exist_ok=True)
    for i, prompt in enumerate(prompts):
        if ":" not in prompt:
            image = pipe(
                prompt,
                height=1024,
                width=1024,
                guidance_scale=3.5,
                num_inference_steps=50,
                max_sequence_length=512,
                generator=torch.Generator("cuda").manual_seed((j+1)*1000)
            ).images[0]

            # Salvataggio immagine
            sanitized_prompt = "_".join(prompt.split())[:100]
            output_path = os.path.join(output_folder, f"image_{i+1}_{sanitized_prompt}.png")
            image.save(output_path)
            exit(0)
