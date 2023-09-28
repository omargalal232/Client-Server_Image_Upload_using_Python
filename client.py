import requests

server_url = 'http://your-server-url/upload_image'

image_path = 'path/to/your/image.jpg'

with open(image_path, 'rb') as image_file:
    response = requests.post(server_url, files={'image': image_file})

if response.status_code == 200:
    print("Image successfully uploaded to the server.")
else:
    print("Failed to upload image to the server.")
