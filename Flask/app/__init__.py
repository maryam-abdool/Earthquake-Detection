from flask import Flask 
from model.inference import Model

app = Flask(__name__)
app.config.from_object("config")

model = Model("model/model.pkl")

from app import views