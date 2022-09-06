from bs4 import BeautifulSoup
import requests
import urllib.request
#from PIL import Image
#from io import BytesIO
#import os

headers={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

r= requests.get("https://www.freeimages.com/search/cat", headers)
soup=BeautifulSoup(r.text, "html.parser")

Images=[]
img_links = soup.select('img[src^="https://images.freeimages.com/images"]')

for i in range(len(img_links)):
    Images.append(img_links[i]['src'])

print(Images)




