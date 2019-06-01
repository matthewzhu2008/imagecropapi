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

| project

--| api.py

--| static

----| images

------| imagetobecropped.png

--| templates

----| cropping.html


Once the necessary installations and folder creations are done, navigate to the folder (in my case, the 'project' folder) that contains the aforementioned files/folders and run with the command

`python api.py`

This will host on your local server which should be listed in cmd prompt behind "Running on " and use a web browser to access it and proceed with uploading the image and choosing coordinates to crop it with. In addition, the name of the file (for example, "imagetobecropped.png") must be placed in the box above "Go" with the placeholder "name of file". The resulting cropped image should then be displayed in the browser and saved in ../static/images as "croppedimg.png".
