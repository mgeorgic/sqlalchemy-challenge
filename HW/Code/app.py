# Import Dependencies
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database and tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the tables
MS = Base.classes.measurement
ST = Base.classes.station
#print(Base.classes.keys())

# Setup the Flask
app = Flask(__name__)

# Flask Routes ("/")
# Define what to do when user hits the index route
@app.route("/")
def home():
    """List of all the available api routes."""
    return(
        f"Welcome to the Climate App API.<br>"
        f"Here are the available routes:<br/>"
        f"<br/>"  
        f"Precipitation Analysis:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"Station Analysis:<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"Temperture Analysis:<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"Start Temperture Analysis:<br/>"
        f"/api/v1.0/start<br/>"
        f"<br/>"
        f"Start and End Temperture Analysis:<br/>"
        f"/api/v1.0/start/end<br/>"
        f"<br/>"
    )
###########################################################

# create precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Retrieve the last 12 months of precipitation data and return the results."""
    year_date = dt.date(2017,8,23) - dt.timedelta(days=365)
    prcp_data = session.query(MS.date, MS.prcp).\
        filter(MS.date >= year_date).\
        order_by(MS.date).all()
    prcp_dict = dict(prcp_data)
    return jsonify(prcp_dict)

# create station route
@app.route("/api/v1.0/stations")
def stations():
        station_total = session.query(ST.station).all()
        station_list = list(station_total)
        stations = list(np.ravel(station_list))
        return jsonify(stations=stations)