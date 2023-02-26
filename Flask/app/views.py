from app import app 
from flask import render_template
from flask import request 
import time as timelibrary

values = set()

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
    values.add(longitude)
    values.add(latitude)
    values.add(date)
    values.add(time)
    timestamp = date + " " + time
    timestamp = timelibrary.mktime(timelibrary.strptime(timestamp, '%Y-%m-%d %H:%M'))
    values.add(timestamp)
    print(values)
    return render_template('index.html', res = values)
