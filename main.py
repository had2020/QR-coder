from flask import Flask, render_template, request, abort, send_from_directory
from flask_cors import CORS
import os
import qrcode
import datetime
import webview # import as pywebview
import random

deletion_due = None

app = Flask(__name__)
CORS(app)

# specify window 
window = webview.create_window('QR Coder', app)

# URL == string

def generate_qrcode(url):
    # QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # adding URL to object
    qr.add_data(url)
    qr.make(fit=True)

    #image path
    time_obj = str(datetime.datetime.now())
    stringged_url = str(url)
    image_folder = "qr-code-pngs/"
    #image_name = stringged_url + time_obj to long names but sometimes works
    #image_path = image_folder + time_obj + ".png"
    image_path = image_folder + str(random.randint(1, 100)) + ".png"

    # create image for code
    img = qr.make_image(fill='black', back_color='white')
    img.save(image_path)

    return(image_path)

@app.route('/')
def index():
  return render_template('index.html')

def delete_file(deletion_due):
  os.remove(deletion_due)

@app.route('/process', methods=['POST', 'GET'])
def process():
  url = request.form['url']
  image_path = str(generate_qrcode(url))
  print(image_path)
  return send_from_directory('qr-code-pngs', os.path.basename(image_path)), delete_file(image_path)
  #return send_from_directory('qr-code-pngs/', image_path)#, delete_file(image_path) TODO FAILS

if __name__ == '__main__':
  #app.run(debug=True, host='0.0.0.0', port=5001) # change to ip and port for non-debug
  webview.start()