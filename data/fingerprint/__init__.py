#!/usr/bin/python
from flask import Flask,render_template
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', time=datetime.datetime.now())
if __name__ == '__main__':
    app.run(debug=True)