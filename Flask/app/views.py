from app import app 
from flask import render_template
from flask import request 
import time as timelibrary
from datetime import datetime

from app import model, gmaps
import geocoder


def getCurLocation():
    return geocoder.ip("me").latlng

def reverse_address(latitude, longitude):
    address = gmaps.reverse_geocode((latitude, longitude))
    return address


@app.route('/')
def my_form():
    print("hi")
    return render_template('index.html')

@app.route("/", methods=["GET", "POST"])
def my_form_post():
    longitude = request.form['longitude'] if request.form["longitude"] else str(getCurLocation()[1])
    latitude = request.form['latitude'] if request.form["latitude"] else str(getCurLocation()[0])
    
    address = reverse_address(latitude, longitude)[0]["address_components"]
    street_number = str(address[0]["long_name"])
    street_name = str(address[1]["long_name"])
    street_info = " ".join((street_number, street_name))
    district = str(address[2]["long_name"])
    city = str(address[3]["long_name"])
    large_city = str(address[4]["long_name"])

    address_detailed = ", ".join((street_info, district))
    address_detailed2 = ", ".join((city, large_city))

    cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date = request.form['date'] if request.form["date"] else cur_time.split(" ")[0]
    time = request.form['time'] if request.form["time"] else ":".join(cur_time.split(" ")[1].split(":")[:-1])
    timestamp = date + " " + time
    timestamp = timelibrary.mktime(timelibrary.strptime(timestamp, '%Y-%m-%d %H:%M'))
    prediction = model.predict((timestamp, latitude, longitude))

    output = "\r\n ".join((address_detailed, address_detailed2, str(prediction)))

    return render_template('index.html', res = output)
