from flask import Flask, render_template, send_file, request, abort
from flask_cors import CORS
from generatecode import generate_qrcode
import os

deletion_due = None

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return render_template('index.html')

def delete_file(deletion_due):
  os.remove(deletion_due)

@app.route('/process', methods=['POST', 'GET'])
def process():
  url = request.form['url']
  image = str(generate_qrcode(url))
  #Todo change this to send you to main page or something
  deletion_due = image
  result = "Button clicked!"
  return send_file(image), render_template('result.html', result=result), delete_file(deletion_due)
  

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5001) # change to ip and port for non-debug