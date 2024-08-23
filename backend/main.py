from flask import Flask, render_template, request
from qrcode import generate_qrcode

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/process', methods=['POST', 'GET'])
def process():
  #Python code to execute here
  generate_qrcode("https://www.example.com/")
  print("button has been clicked!")
  result = "Button clicked!"
  return render_template('result.html', result=result)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000) # change to ip and port for non-debug