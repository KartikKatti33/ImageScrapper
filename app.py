# Author: Kartik Katti

from flask_cors import CORS,cross_origin
from flask import Flask, render_template, request, jsonify
import os
from scrapperImage.ScrapperImage import ScrapperImage
from businesslayer.BusinessLayerUtil import BusinessLayer

app= Flask(__name__)

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')
    print('done')

@app.route('/showImages')
@cross_origin()
def displayImages():
    list_images=os.listdir('Static')
    print(list_images)

    try:
        if(len(list_images)>0):
            return render_template('showImage.html', user_images=list_images)
        else:
            return "Images not present"
    except Exception as e:
        print("No images found", e)
        return "Please try again"

@app.route('/searchImages', methods=['Get','POST'])
def searchImage():
    if request.method=='POST':
        search_term=request.form['keyword']
        print("search term: ", search_term)

    else:
        print("Please enter something")

    imagescrapperutil=BusinessLayer
    imagescrapper=ScrapperImage()
    list_images=os.listdir('Static')
    print(list_images)
    imagescrapper.delete_downloaded_images(list_images)

    image_name=search_term.split()
    image_name="-".join(image_name)
    print(image_name)

    header={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
            
            }

    lst_images=imagescrapperutil.downloadImages(search_term,header)

    return displayImages()



if __name__=="__main__":
    app.run(host='127.0.0.1', port=8000)