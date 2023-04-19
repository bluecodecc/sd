from image_server import ImageServer
from stable_diffusion import StableDiffusion

if __name__ == '__main__':
    stable_diffusion = StableDiffusion("")
    image_server = ImageServer("", "", "")
    payload = {
        "sd_model_checkpoint": "chilloutmix_NiPrunedFp32Fix",
        "prompt": "(RAW photo, best quality), (realistic, photo-realistic:1.3), best quality ,masterpiece, an extremely delicate and beautiful, extremely detailed ,CG ,unity ,2k wallpaper, Amazing, finely detail, masterpiece,light smile,best quality, extremely detailed CG unity 8k wallpaper,huge filesize , ultra-detailed, highres, extremely detailed, iu,asymmetrical bangs,short bangs,bangs,pureerosface_v1,beautiful detailed girl, extremely detailed eyes and face, beautiful detailed eyes,light on face,looking at viewer, straight-on, staring, closed mouth,black hair,long hair, collarbone, bare shoulders, longeyelashes,breasts,nipples,upper body, lace ,lace trim,1girl,nude, naked girl, (full body:1.3), (highly detail face: 1.5), (beautiful ponytail:0.5),beautiful detailed eyes, beautiful detailed nose, vaginal detailed, nipples, realistic face, realistic body, beautiful pussy, pussy detail, comfortable expressions, thigh spread,smile, look at viewer,(ass to camera:1.1),comfortable expressions, ((thigh spread)), (ass in the mirror:1.1),ass detail,<lora:koreanDollLikeness_v10:0.3> , <ulzzang-6500:0.4>",
        "negative_prompt": "bra, covered nipples, underwear,EasyNegative, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans,extra fingers,fewer fingers,((watermark:2)),(white letters:1), (multi nipples), lowres, bad anatomy, bad hands, text, error, missing fingers,extra digit, fewer digits, cropped, worst quality, low qualitynormal quality, jpeg artifacts, signature, watermark, username,bad feet, {Multiple people},lowres,bad anatomy,bad hands, text, error, missing fingers,extra digit, fewer digits, cropped, worstquality, low quality, normal quality,jpegartifacts,signature, watermark, blurry,bad feet,cropped,poorly drawn hands,poorly drawn face,mutation,deformed,worst quality,low quality,normal quality,jpeg artifacts,signature,extra fingers,fewer digits,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,text,error,missing fingers,missing arms,extra arms,missing legs,wrong feet bottom render,extra digit,abdominal stretch, glans, pants, briefs, knickers, kecks, thong, {{fused fingers}}, {{bad body}}",
        "sampler_index": "DPM++ SDE Karras",
        "steps": 30,
        "restore_faces": True,
        "enable_hr": True,
        "denoising_strength": 0.7,
        "firstphase_width": 512,
        "firstphase_height": 512,
        "hr_scale": 3,
        "hr_upscaler": "Latent",
        "hr_second_pass_steps": 30,
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
