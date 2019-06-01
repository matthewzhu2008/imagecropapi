# Image Crop API
Uploads and crops image and saves it as croppedimg.png within the images folder
- Acceptable image file formats: txt, png, pdf, jpg, jpeg, gif

# Installations necessary:
python 3.7+ (latest version ideal)
pip
Pillow (program uses PIL for cropping)

`pip install pillow`

# Setup
A static and template folder need to be created in the same folder as api.py and an images folder needs to be created within the static folder with the images you want to be cropped. Additionally, put the file cropping.html in the templates folder.

My directory looks like the following:

--| api.py

--| static

----| images

------| imagetobecropped.png

--| templates

----| cropping.html
