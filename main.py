# import required modules
from flask import Flask, render_template, request
from src.utils import *
from src.detect import *

# create flask app
app = Flask(__name__)

# main route (show html page)
@app.route('/')
def index():
    return render_template('index.html')

# api endpoint for image upload
@app.route('/api/upload', methods=['POST'])
def upload():
    # receive the file from the client
    file = request.files['file']
    filepath = f'static/temp/{file.filename}'
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    file.save(os.path.join(APP_ROOT, filepath)) # save to directory

    # process image after upload
    process_image(os.path.join(APP_ROOT, filepath))
    
    # return server url to client
    return f"{request.url_root}{filepath}"

# Run flask server
if __name__ == '__main__':
    app.run(debug=True) # set debug true to load reload server auto on changes