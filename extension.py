#below is made using the help of cs50.ai
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index.html')
def home():
    message = "Hello, CS50!!"
    return render_template('index.html', message=message)