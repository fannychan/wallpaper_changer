import requests
import shutil
import ctypes
import os

params = {
    'client_id': '025823c4d110f90bcc8e16393459192e4595cb4671443f3d4ca3e0018d5e71c1',
    'query': 'flowers,landscape,office,home,spring',
    'orientation': 'landscape',
}

r = requests.get('https://api.unsplash.com/photos/random', params=params)
json = r.json()
# print(json)

path = 'C:\\Users\\chanf\\PycharmProjects\\wallpaper\\img.png'

url = json['urls']['raw']
response = requests.get(url, stream=True)
with open(path, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)

# path = os.path.abspath("img.png")
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)




#print(r)