from app import app
from flask import render_template, request, url_for
import os, base64

# Index
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from functions import create_image
        
        # create_image function from functions.py, pass it the entire request form object.
        # This function creates our image for us
        create_image(request.form)
        
        # We need to open the image back up so that it can be encoded
        imgfile = open('app/static/quote.PNG')
        
        # Encode it as base64 for use in the template (cache issue resolved)
        imagesrc = base64.b64encode(imgfile.read())
        
        # A return to tell our template to display the image
        display = True
    else:
        # Don't display
        display = False
        imagesrc = False
    
    # Our list of fonts. 
    # These fonts have to be TTF!!
    fonts = [font.rstrip('.ttf') for font in os.listdir('app/static/fonts') if font.endswith('.ttf')]
    
    return render_template('index.html', fonts = fonts, display = display, imagesrc = imagesrc)