import os
from PIL import Image
import webp

directory = '/home/yuri/Imagens/TESTE'
output_format = '.webp'

for filename in os.listdir(directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
        image_path = os.path.join(directory, filename)
        img = Image.open(image_path)

        webp_path = os.path.join(directory, os.path.splitext(filename)[0] + output_format)
        img.save(webp_path, format='WEBP', quality=80)

        print(f"Converted {filename} to {output_format}")