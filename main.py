from image_server import ImageServer
from stable_diffusion import StableDiffusion

if __name__ == '__main__':
    stable_diffusion = StableDiffusion("")
    image_server = ImageServer("", "", "")
    payload = {
        "sd_model_checkpoint": "3Guofeng3_v33.safetensors",
        "prompt": "best quality, masterpiece, highres, 1girl,blush,(seductive smile:0.8),star-shaped pupils,china hanfu,hair ornament,necklace, jewelry,Beautiful face,upon_body, tyndall effect,photorealistic, dark studio, rim lighting, two tone lighting,(high detailed skin:1.2), 8k uhd, dslr, soft lighting, high quality, volumetric lighting, candid, Photograph, high resolution, 4k, 8k, Bokeh",
        "negative_prompt": "(((simple background))),monochrome ,lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, lowres, bad anatomy, bad hands, text, error, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, ugly,pregnant,vore,duplicate,morbid,mut ilated,tran nsexual, hermaphrodite,long neck,mutated hands,poorly drawn hands,poorly drawn face,mutation,deformed,blurry,bad anatomy,bad proportions,malformed limbs,extra limbs,cloned face,disfigured,gross proportions, (((missing arms))),(((missing legs))), (((extra arms))),(((extra legs))),pubic hair, plump,bad legs,error legs,username,blurry,bad feet",
        "sampler_index": "DPM++ SDE Karras",
        "steps": 25,
        "restore_faces": True,
        "enable_hr": True,
        "denoising_strength": 0.7,
        "firstphase_width": 512,
        "firstphase_height": 512,
        "hr_scale": 2,
        "hr_upscaler": "Latent",
        "hr_second_pass_steps": 25,
        "hr_resize_x": 0,
        "hr_resize_y": 0,
        "cfg_scale": 8.5,
        "seed": -1,
    }
    while True:
        images = stable_diffusion.text_to_image(payload)
        for image in images:
            response = image_server.upload_image(image=image)
            print(response)
