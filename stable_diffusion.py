import requests
import io
import base64
from PIL import Image, PngImagePlugin


class StableDiffusion:
    def __init__(self, url):
        self.url = url

    def text_to_image(self, payload):
        url = f'{self.url}/txt2img'
        response = requests.post(url=url, json=payload).json()
        images: list = []
        for image_data in response.get("images"):
            info = self.get_img_info(image_data)
            image = Image.open(io.BytesIO(base64.b64decode(image_data.split(",", 1)[0])))
            # image.info = info
            images.append(image)
        return images

    def get_img_info(self, image):
        payload = {
            "image": "data:image/png;base64," + image
        }
        url = f'{self.url}/png-info'
        response = requests.post(url=url, json=payload).json()
        png_info = PngImagePlugin.PngInfo()
        png_info.add("info", response.get("info"))
        return png_info
