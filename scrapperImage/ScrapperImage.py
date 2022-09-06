from bs4 import BeautifulSoup as bs
import os
import json
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlretrieve
import requests

class ScrapperImage:

    def createImageUrl(searchterm):
        print("searchterm:" , searchterm)
        searchterm=searchterm.split()
        searchterm="-".join(searchterm)
        web_url="https://www.freeimages.com/search/"+ searchterm
        print(web_url)
        return web_url

    def scrap_html_data(url,header):
       # request=urllib.request.Request(url, headers=header)
       # response= urllib.request.urlopen(request)
       # responseData = response.read()
       # html= bs(responseData,'html.parser')
        r= requests.get(url, header)
        soup=bs(r.text, "html.parser")
        return soup

    def getimageUrlList(rawHtml):
       
        Images=[]
        img_links = rawHtml.select('img[src^="https://images.freeimages.com/images"]')

        for i in range(len(img_links)):
            Images.append(img_links[i]['src'])

        print("there are total", len(Images), "images")
        return Images

    def downloadImagesFromURL(imageUrlList, image_name, header):
        masterListOfImages=[]
        count=0
        imageFiles=[]
        imagetypes=[]
        image_counter=0
        for img in imageUrlList:
            try:
                if(count>5):
                    break
                else:
                    count=count+1
                req=urllib.request.Request(img, headers=header)
                try:
                    urllib.request.urlretrieve(img, "./Static/"+image_name+str(image_counter)+".jpg")
                    image_counter=image_counter+1
                except Exception as e:
                    print("Image write failed", e)
                    image_counter=image_counter+1
                respData = urllib.request.urlopen(req)
                raw_image = respData.read()
                imageFiles.append(raw_image)
                imagetypes.append(".jpg")

            except Exception as e:
                print("could not load img", e)
                count=count+1

        masterListOfImages.append(imageFiles)
        masterListOfImages.append(imagetypes)

        return masterListOfImages

    def delete_downloaded_images(self,list_of_images):
        for self.image in list_of_images:
            try:
                os.remove("./Static/"+self.image)
                print("delete successful")
            except Exception as e:
                print("error in deleting: ", e)

        return 0













