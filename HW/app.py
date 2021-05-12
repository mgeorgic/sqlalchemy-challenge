# Import Dependencies
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect an existing database and tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the tables
MS = Base.classes.measurement
ST = Base.classes.station
print(Base.classes.keys())
# Shows both tables so I am connected

# Setup the Flask
app = Flask(__name__)

# Flask Routes ("/")
# Define what to do when user hits the index route
@app.route("/")
def home():
    """List of all the available api routes."""
    return(
        f"Welcome to the Climate App API!.<br>"
        f"<br/>"
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
    prcp = session.query(MS.date, MS.prcp).\
        filter(MS.date >= year_date).\
        order_by(MS.date).all()
    prcp_dict = dict(prcp)
    return jsonify(prcp_dict)

# create station route
@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations"""
    station_total = session.query(ST.station).all()
    station_list = list(station_total)
    stations = list(np.ravel(station_list))
    return jsonify(stations = stations)

# creat TOBs route
@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of temperature observations for the previous year"""
    year_date = dt.date(2017,8,23) - dt.timedelta(days=365)
    tobs = session.query(MS.tobs).\
        filter(MS.date >= year_date).\
        order_by(Ms.date).all()
    tobs_list = list(np.ravel(tobs))
    return jsonify(tobs_list = tobs_list)

@app.route("/api/v1.0/<start>")
def start(start=None):
    # Docstring
    """Return a JSON list of tmin, tmax, tavg for the dates greater than or equal to the date provided"""

    start_only = session.query(MS.date, func.min(MS.tobs), func.avg(MS.tobs),
                               func.max(MS.tobs)).filter(MS.date >= start).group_by(
        Measurement.date).all()
    start_list = list(start_only)
    return jsonify(start_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start=None, end=None):
    # Docstring
    """Return a JSON list of tmin, tmax, tavg for the dates in range of start date and end date inclusive"""

    start_end = session.query(MS.date, func.min(MSt.tobs), func.avg(MS.tobs),
                                  func.max(MS.tobs)).filter(MS.date >= start).filter(
        Measurement.date <= end).group_by(MS.date).all()
    start_end_list = list(start_end)
    return jsonify(start_end_list)

if __name__ == "__main__":
    app.run()