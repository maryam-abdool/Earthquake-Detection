from app import app 
from flask import render_template
from flask import request 
import time as timelibrary
from datetime import datetime

from app import model


@app.route('/')
def my_form():
    print("hi")
    return render_template('index.html')

@app.route("/", methods=["GET", "POST"])
def my_form_post():
    longitude = request.form['longitude'] if request.form["longitude"] else "0"
    latitude = request.form['latitude'] if request.form["latitude"] else "0"
    cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date = request.form['date'] if request.form["date"] else cur_time.split(" ")[0]
    time = request.form['time'] if request.form["time"] else ":".join(cur_time.split(" ")[1].split(":")[:-1])
    timestamp = date + " " + time
    timestamp = timelibrary.mktime(timelibrary.strptime(timestamp, '%Y-%m-%d %H:%M'))
    prediction = model.predict((timestamp, latitude, longitude))

    return render_template('index.html', res = prediction)
