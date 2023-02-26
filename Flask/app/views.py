from app import app 
from flask import render_template
from flask import request, url_for, redirect
import time as timelibrary
from datetime import datetime

from app import model, gmaps
import geocoder
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import os

class ERROR_CODES:
    SUCCESS = 0
    INVALID_LONGITUDE = -1 
    INVALID_LATITUDE = -2
    INVALID_DATETIME = -3


def getCurLocation():
    return geocoder.ip("me").latlng

def reverse_address(latitude, longitude):
    address = gmaps.reverse_geocode((latitude, longitude))
    return address

def checkForm(form: dict):
    try:
        if (float(form["longitude"]) > 180 or float(form["longitude"]) <= -180):
            raise "INVALID_LONGITUDE"
    except:
        return ERROR_CODES.INVALID_LONGITUDE
    
    try:
        if (float(form["latitude"]) > 90 or float(form["latitude"]) <= -90):
            return ERROR_CODES.INVALID_LATITUDE
    except:
        return ERROR_CODES.INVALID_LATITUDE
    return ERROR_CODES.SUCCESS

@app.route('/')
def my_form():
    print("hi")
    return render_template('index.html')

@app.route("/", methods=["GET", "POST"])
def my_form_post():
    longitude = request.form['longitude'] if request.form["longitude"] else str(getCurLocation()[1])
    latitude = request.form['latitude'] if request.form["latitude"] else str(getCurLocation()[0])

    code = checkForm(request.form)
    
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

    output = [address_detailed, address_detailed2, str(prediction)]

    map = Basemap(projection='lcc', 
                resolution=None,
                width=16E6, height=9E6, 
                lat_0=latitude, lon_0=longitude,)
    map.etopo(scale=1, alpha=1)
    x, y = map(longitude, latitude)
    plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y, " " + city, fontsize=12)
    plt.savefig("app/static/img/local_map.png", transparent=True)
    return redirect(url_for("show", output="&&".join(output))) 

@app.route("/result/?<string:output>", methods=["GET"])
def show(output):
    output = output.split("&&")
    return render_template("result.html", res = output)


@app.route("/result/?<string:output>", methods=["POST"])
def get_back(output):
    print("get back")
    return redirect(url_for('my_form'))
