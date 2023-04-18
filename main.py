from image_server import ImageServer
from stable_diffusion import StableDiffusion

if __name__ == '__main__':
    stable_diffusion = StableDiffusion("http://server.404996.xyz:7860/sdapi/v1")
    image_server = ImageServer("http://pic.404996.xyz:6060/api/v1", "1039755466@qq.com", "ZKmJLtCSccd8wJj")
    payload = {
        "sd_model_checkpoint": "chilloutmix_NiPrunedFp32Fix.safetensors",
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
    images = stable_diffusion.text_to_image(payload)
    for image in images:
        response = image_server.upload_image(image=image)
        print(response)
