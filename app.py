from PIL import Image
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/classify/', methods=['POST'])
def classify():
    f = request.files['img']
    filename = secure_filename(f.filename) 
    f.save(filename)
    im = Image.open(filename).convert("RGB")

    pixels = [im.getpixel((i,j)) for j in range(im.height) for i in range(im.width)]

    cond = (255, 194, 231) in pixels or (255, 165, 217) in pixels or (252, 215, 222) in pixels or (73, 186, 77) in pixels
    os.remove(filename)
    if cond:
        return "Peppa Pig"
    else:
        return "Assassin's Creed"

if __name__ == '__main__':
    app.run()