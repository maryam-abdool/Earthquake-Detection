from flask import Flask 
from model.inference import Model
import googlemaps
import config

app = Flask(__name__)
app.config.from_object("config")

model = Model("model/model.pkl")

gmaps = googlemaps.Client(key=config.GOOGLEMAP_KEY)

from app import views