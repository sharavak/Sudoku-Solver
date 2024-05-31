from flask import Flask,request
import json
import os
from flask import Response,jsonify
from flask_cors import CORS
from extract import imageExtraction
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader

load_dotenv()
app=Flask(__name__)
CORS(app)
cloudinary.config( 
    cloud_name = os.getenv("CLOUD_NAME"), 
    api_key = os.getenv("API_KEY"),
    api_secret = os.getenv("API_SECRET"),
    secure=True
)
@app.route("/",methods=['GET','POST'])
def main():
    if request.method=='POST':
        file=request.files['image']
        image=cloudinary.uploader.upload(file)
        board=imageExtraction(image['secure_url'],0)
        cloudinary.uploader.destroy(image['public_id'])
        return Response(json.dumps({"data":board}),mimetype="application/json")
    return Response("HI")
app.run(debug=True)