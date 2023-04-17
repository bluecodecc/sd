import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin

url = "http://server.404996.xyz:7860"
# We need to set the sampling method in the payload dictionary before making the API request
# There are different sampling methods available, such as greedy, nucleus, top-k, and top-p
# We can set the sampling method by adding a "sampling_method" key to the payload dictionary with the desired value

payload = {
    "sd_model_checkpoint": "chilloutmix_NiPrunedFp32Fix.safetensors [fc2511737a]",
    "prompt": "a girl is standing in the shower,1girl,unbuttoned shirt,lipstick,hair bun,colored inner hair,shushing,{steam},Looking at Viewer,golden hour lighting,comic,atmospheric perspective,bokeh,detailed,Cinematic light, intricate detail, highres, detailed facial features, high detail, sharp focus, smooth, aesthetic, extremely detailed, stamp, octane render,{{{masterpiece}}},full-body shot",
    "sampler_index": "DPM++ 2S a Karras",
    "steps": 20,
    "restore_faces": True,
    "enable_hr": True,
    "denoising_strength": 0.7,
    "firstphase_width": 512,
    "firstphase_height": 512,
    "hr_scale": 2,
    "hr_upscaler": "Latent",
    "hr_second_pass_steps": 20,
    "hr_resize_x": 0,
    "hr_resize_y": 0,
    "cfg_scale": 6,
    "seed": -1,
}


response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

r = response.json()

for i in r['images']:
    image = Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0])))

    png_payload = {
        "image": "data:image/png;base64," + i
    }
    response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

    pnginfo = PngImagePlugin.PngInfo()
    pnginfo.add_text("parameters", response2.json().get("info"))
    print(response2.json().get("info"))
    image.save('output.png', pnginfo=pnginfo)


