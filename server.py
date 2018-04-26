import random
import json
import requests
from flask import (Flask,
                   request,
                   url_for,
                   render_template)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/data.json")
def data():
    # TODO read temperature and humidity from Arduino
    s = serial.Serial("/dev/ttyACM0")  
    l = s.readline() 
    #check to see if l is x's and print errors (print ???)
    if(l == "X"):
	indoor_temp == "???"
	indoor_humidity == "???"
    else:
        x = l.rstrip().split(",")
        indoor_temp = x[0]
        indoor_humidity = x[1]
	
    # read temperature and humidity from openweathermap.org
    r = request.get("http://api.openweathermap.org/data/2.5/"+
		    "weather?id=4347242&units=imperial&"+
		    "APPID=09f303a8a7a78820feda94e4d2ee47d6")
    data = r.json()
    outdoor_temp = data['main']['temp']
    outdoor_humidity = data['main']['humidity']
    # send the result as JSON
    return json.dumps({
        "indoor_temp": indoor_temp,
        "indoor_humidity": indoor_humidity,
        "outdoor_temp": outdoor_temp,
        "outdoor_humidity": outdoor_humidity})


@app.route("/cheep",methods=['POST'])
def cheep():
    name = request.form['name']
    message = request.form['message']
    print("got a cheep from [%s]: %s" % (name,message))
    # TODO: append [name: message] to a file of cheeps
    # TODO: display the cheep on the kit LCD
    return render_template('thankyou.html')
