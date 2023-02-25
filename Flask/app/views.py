from app import app 
from flask import render_template
from flask import request 

values = set()

@app.route('/')
def my_form():
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
    #print(values)
    return render_template('index.html', res = values)
