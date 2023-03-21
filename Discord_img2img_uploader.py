import os
import time
from datetime import datetime
from PIL import Image
from discord_webhook import DiscordWebhook, DiscordEmbed

# Configuration variables
SCAN_INTERVAL = 30  # Time between scnans for new image files
PHOTOS_ROOT_DIR = "outputs/img2img-images"
LAST_UPLOAD_FILE = "last_img2img_upload.txt"
WEBHOOK_URL = "PASTE TOKEN HERE"

# Create Discord webhook object
webhook = DiscordWebhook(url=WEBHOOK_URL)

# Load the time of the last upload from a file
try:
    with open(LAST_UPLOAD_FILE) as f:
        last_upload_str = f.read().strip()
        last_upload = float(last_upload_str) if last_upload_str else 0.0
except FileNotFoundError:
    last_upload = 0.0


while True:
    for subdir, dirs, files in os.walk(PHOTOS_ROOT_DIR):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                photo_path = os.path.join(subdir, file)
                photo_mod_time = os.path.getmtime(photo_path)
                if photo_mod_time > last_upload:
                    # Metadata extraction
                    with Image.open(photo_path) as image:
                        img_data = image.info.get("parameters", "")
                        model_name = img_data.rsplit("Model: ", 1)[-1].strip()
                        img_data = img_data.replace("Negative prompt:", "\nNegative prompt:").replace("Steps:", "\nSteps:")

                        # Add the image file as an attachment to the Discord message
                        with open(photo_path, "rb") as f:
                            webhook.add_file(file=f.read(), filename=file)
                        
                    # Construct the Discord embed object and send the message via webhook API
                    embed = DiscordEmbed(
                        title="New img2img generation",
                        description=img_data,
                        color=0xe800db,
                        timestamp=datetime.now().isoformat(),
                    )
                    embed.set_image(url=f"attachment://{file}")
                    embed.add_embed_field(name="Model", value=model_name)
                    embed.set_footer(text="Stable Diffusion txt2img")
                    webhook.add_embed(embed)
                    response = webhook.execute(remove_embeds=True)

                    # Update the time of the last upload
                    last_upload = max(last_upload, photo_mod_time)
                    with open(LAST_UPLOAD_FILE, "w") as f:
                        f.write(str(last_upload))

    time.sleep(SCAN_INTERVAL)
