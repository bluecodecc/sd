import requests


class ImageServer:
    def __init__(self, url, email, password):
        self.url = url
        self.email = email
        self.password = password
        self.token = None
        self.init_token()

    def init_token(self):
        url = f'{self.url}/tokens'
        data = {"email": self.email, "password": self.password}
        response = requests.post(url=url, data=data)
        token = response.json().get('data').get('token')
        if token is None:
            raise Exception("Token is None")
        self.token = token

    def upload(self, image_path):
        with open(image_path, 'rb') as file:
            return self.upload_image(file)

    def upload_image(self, image):
        url = f'{self.url}/upload'
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
        }
        files = {'file': image}
        return requests.post(headers=headers, url=url, files=files).json()


def images(self):
    url = f'{self.url}/images'
    headers = {"Authorization": f"Bearer {self.token}", "Accept": "application/json", }
    return requests.get(headers=headers, url=url)
