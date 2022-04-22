from distutils.log import debug
from flask import Flask, redirect, url_for, request, render_template, session

import os, uuid, json, requests


from dotenv import load_dotenv
load_dotenv()


app = Flask (__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def captionGenerator():
    imageSelected = request.form['ImageSelected']

    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']

    path = '/vision/v3.1/analyze'
    constructedURL = endpoint + path

    headers = {'Ocp-Apim-Subscription-Key': key}
    params = {'visualFeatures': 'Description'}
    data = {'url': str(imageSelected)}

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    response = requests.post(constructedURL, headers=headers, params=params, json=data)
    response.raise_for_status()
    analysis = json.loads(response.text)    
    conf=analysis['description']['captions'][0]['confidence'],
    conf=conf[0]
    imageCapCon=conf*100
    imageCapCon="{:2f}".format(imageCapCon)
    
    return render_template(
        'imageCaption.html', 
        ImageSelected=str(imageSelected),
        imageCap=analysis['description']['captions'][0]['text'],
        imageTags=analysis['description']['tags'],
        imageCapCon=imageCapCon
        
        
    )