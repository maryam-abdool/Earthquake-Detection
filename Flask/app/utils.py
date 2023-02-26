from time import mktime, strptime
from dataclasses import dataclass
from geocoder import ip 
from datetime import datetime


class ERROR_CODES:
    SUCCESS = 0
    INVALID_LONGITUDE = -1 
    INVALID_LATITUDE = -2
    INVALID_DATETIME = -3

def strToTimestamp(s):
    timestamp = mktime(strptime(s, '%Y-%m-%d %H:%M:%S'))
    return timestamp

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
    
    try:
        timestr = form['date'] + " " + form['time']
        print(timestr)
        timestamp = strToTimestamp(timestr)
    except:
        return ERROR_CODES.INVALID_DATETIME 
    return ERROR_CODES.SUCCESS

def fillFormByDefault(form: dict):
    if not form.get("longitude", "") or not form.get("latitude", ""):
        form.update(getCurrentIPLatLng())
        
    curr_datetime = getCurrentDatetime()

    if not form.get("date", ""):
        form.update({"date": curr_datetime.split()[0]})
    if not form.get("time", ""):
        form.update({"time": curr_datetime.split()[1]})
    return 
        

def getCurrentIPLatLng():
    g = ip('me')
    return {"latitude": g.latlng[0], "longitude": g.latlng[1]}

def getCurrentDatetime():
    return str(datetime.now())[: 19]
    
    
if __name__ == "__main__":
    print(getCurrentDatetime())
    print(strToTimestamp("2023-02-26 02:51:25"))
    