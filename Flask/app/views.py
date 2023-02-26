from app import app 
from flask import render_template
from flask import request 
import time as timelibrary

from model import inference


@app.route('/')
def my_form():
    print("hi")
    return render_template('index.html')

@app.route("/", methods=["GET", "POST"])
def my_form_post():
    longitude = request.form['longitude']
    latitude = request.form['latitude']
    date = request.form['date']
    time = request.form['time']
    timestamp = date + " " + time
    timestamp = timelibrary.mktime(timelibrary.strptime(timestamp, '%Y-%m-%d %H:%M'))
    prediction = inference.predict((timestamp, latitude, longitude))
    print(prediction)

    #print(values)
    return render_template('index.html', res = prediction)
