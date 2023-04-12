# Stable diffusion discord upploader

Stable Diffusion Discord Uploader is a Python script that automatically extracts metadata and uploads newly generated images as embeds to Discord using Discord's Webhook API. This script is meant to be used with the Windows version of [AUTOMATIC1111 stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui). The Discord embeds include the generated image, positive and negative prompts extracted from metadata, as well as steps, sampler, CFG scale, seed, resolution, model hash, and model name. By default, the script is configured to upload `txt2img` and `img2img` but can easily be configured, under `configuration variables`, to upload other types of generations.



![image](https://github.com/Harren06/Stable-diffusion-discord-upploader/blob/main/image.png)

## installation
- Install the dependencies
```
pip install discord-webhook
``` 
- Download [Latest release](https://github.com/Harren06/Stable-diffusion-discord-upploader/releases/latest)
- Extrct in root folder of [AUTOMATIC1111 stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- Replace `webui-user.bat` (or add `start /B python Discord_txt2img_uploader.py` and `start /B python Discord_img2img_uploader.py` before `call webui.bat`)
- Paste your Discord webhook URL in the `WEBHOOK_URL` variable in both `Discord_txt2img_uploader.py` and `Discord_txt2img_uploader.py`. If you want the images to be uploaded to different Discord channels, you can use different URLs.

- Time between scans and image directory can be changed under `Configuration variables`

## Donate
Donate to support my current and future projects!
- Bitcoin `bc1qesn6yragltvvztjjuw05alhyd88l2mev288gvg` 
- Monero `48tAQeqAjuUhk68mY18oK4DZ9rBzPk6WJWFwcTKE42obJSjP9rj6oqmaFZLoWrrT6X37VNxRB8Kd9WR386FTnkpcC1SBX6X`
- Ravencoin `RB7n2YN6SK8NTRPDEvwB9jWvfjTPaF6prE`

## Used By

This project is used by the following companies:

- Your mom
