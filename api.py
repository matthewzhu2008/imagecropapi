from flask import Flask, url_for, send_from_directory, request, redirect, render_template
import logging, os
from werkzeug import secure_filename
from PIL import Image


#saves uploaded image to uploads folder located in C: (must create folder ahead of time)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config["DEBUG"] = True

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            return render_template('cropping.html', filename=filename)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory("static/images", filename)

# crop filename from (x1,y1) to (x2,y2)
@app.route("/crop", methods=["POST"])
def crop():
    # retrieve parameters from html form
    x1 = int(request.form['x1'])
    y1 = int(request.form['y1'])
    x2 = int(request.form['x2'])
    y2 = int(request.form['y2'])
    filename = request.form['image']

    # open image
    target = os.path.join(APP_ROOT, 'static/images')
    destination = "/".join([target, filename])

    img = Image.open(destination)

    # check for valid crop parameters
    width = img.size[0]
    height = img.size[1]

    crop_possible = True
    if not 0 <= x1 < width:
        crop_possible = False
    if not 0 < x2 <= width:
        crop_possible = False
    if not 0 <= y1 < height:
        crop_possible = False
    if not 0 < y2 <= height:
        crop_possible = False
    if not x1 < x2:
        crop_possible = False
    if not y1 < y2:
        crop_possible = False

    # crop image and show
    if crop_possible:
        img = img.crop((x1, y1, x2, y2))
        
        # save and return image
        destination = "/".join([target, 'croppedimg.png'])
        if os.path.isfile(destination):
            os.remove(destination)
        img.save(destination)
        return uploaded_file('croppedimg.png')
    return '', 204



app.run()