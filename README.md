# Stable diffusion discord upploader

Stable diffusion discord upploader is a python script that automaticly extracts metadata and upploads newly genereatd images as embeds to Discord using Discords webhook API. This script is ment to be used with thw windows version of [AUTOMATIC1111 stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui). The Discord embeds include the image generaded, positive and negative promts extracted from metadata, as well as steps, sampler, CFG scale, seed, resolution, model hash and model name. By default the script is configured to upload `txt2img` and `img2img` but can easily be configured under `Configuration variables` to uppload other types of generations.

![image](https://github.com/Harren06/Stable-diffusion-discord-upploader/blob/main/image.png)

## Instalation
- Install the dependencies
```
pip install discord-webhook
``` 
- Download [Latest release](https://github.com/Harren06/Stable-diffusion-discord-upploader/releases/latest)
- Extrct in root folder of [AUTOMATIC1111 stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- Replace `webui-user.bat` (or add `start /B python Discord_txt2img_uploader.py` and `start /B python Discord_img2img_uploader.py` before `call webui.bat`)
- Add Discord webhook API url in `WEBHOOK_URL variable under` `Configuration variables`
- Time between scans and image directory can be changed under `Configuration variables`

## Donate
Donate to support my current and future projects!
- Bitcoin: `bc1qesn6yragltvvztjjuw05alhyd88l2mev288gvg` 

## Used By

This project is used by the following companies:

- Your mom
