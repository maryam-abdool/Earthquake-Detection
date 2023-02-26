from time import mktime, strptime
from dataclasses import dataclass


class ERROR_CODES:
    SUCCESS = 0
    INVALID_LONGITUDE = -1 
    INVALID_LATITUDE = -2
    INVALID_DATETIME = -3

def strToTimestamp(s):
    timestamp = mktime(strptime(s, '%Y-%m-%d %H:%M'))
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
        timestamp = strToTimestamp(timestr)
    except:
        return ERROR_CODES.INVALID_DATETIME 
    return ERROR_CODES.SUCCESS
    