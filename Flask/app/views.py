from app import app 
from flask import render_template
from flask import request 
from app.utils import strToTimestamp, ERROR_CODES, checkForm

from app.models import model

@app.route('/')
def my_form():
    print("hi")
    return render_template('index.html')

@app.route("/", methods=["GET", "POST"])
def my_form_post():
    error_code = checkForm(request.form)
    res = {}
    print("error_code", error_code==ERROR_CODES.INVALID_LATITUDE)
    if error_code == ERROR_CODES.INVALID_LONGITUDE:
        res = {"ERROR": "Invalid Longitude Value."}
    elif error_code == ERROR_CODES.INVALID_LATITUDE:
        res = {"ERROR": "Invalid Latitude Value."}
    elif error_code == ERROR_CODES.INVALID_DATETIME:
        res = {"ERROR": "Invalid Datetime."}
    else:
        longitude = request.form['longitude']
        latitude = request.form['latitude']
        timestr = request.form['date'] + " " + request.form['time']
        timestamp = strToTimestamp(timestr)
        print(dir(model))
        res = {"Prediction": model.predict((timestamp, latitude, longitude))}
    return render_template('index.html', res = res)