from flask import Flask, flash, request, url_for, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ALLOWED_EXTENSIONS = set(['tiff', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/', methods=['GET'])
def index():
    return "Success"

@app.route('/results', methods=['POST'])
#todo: accept only images
def results():
    if 'image' not in request.files:
        return 'there is no image in form!'
    image = request.files['image']
    if image.filename == '':
         return 'No selected file'
    if not image:
        return "Image is null"
    elif not allowed_file(image.filename):
        return "uploaded file is not an image"
    res = hasPneumonia(image)
    image.close()
    return jsonify(res)

def hasPneumonia(image):
    return False

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run()