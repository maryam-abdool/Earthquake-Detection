from app import app 
from flask import render_template
from flask import request 
from app.utils import strToTimestamp, ERROR_CODES, checkForm, getCurrentIPLatLng, getCurrentDatetime, fillFormByDefault

from app.models import model

@app.route('/')
def my_form():
    print("hi")
    return render_template('index.html')

@app.route("/", methods=["GET", "POST"])
def my_form_post():
    form = dict(request.form) 
    print(form)
    fillFormByDefault(form)
    error_code = checkForm(form)
    res = {}
    if error_code == ERROR_CODES.INVALID_LONGITUDE:
        res = {"ERROR": "Invalid Longitude Value."}
    elif error_code == ERROR_CODES.INVALID_LATITUDE:
        res = {"ERROR": "Invalid Latitude Value."}
    elif error_code == ERROR_CODES.INVALID_DATETIME:
        res = {"ERROR": "Invalid Datetime."}
    else:
        longitude = form['longitude']
        latitude = form['latitude']
        timestr = form['date'] + " " + form['time']
        timestamp = strToTimestamp(timestr)
        res = {"Prediction": model.predict((timestamp, latitude, longitude))}
    return render_template('index.html', res = res)