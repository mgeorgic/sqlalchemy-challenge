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

# Create our session (link) from Python to the DB
session = Session(engine)

# Setup the Flask
app = Flask(__name__)

# Flask Routes ("/")
# Define what to do when user hits the index route
@app.route("/")
def home():
    """List of all the available api routes."""
    return(f'''
        Welcome to the Climate App API!<br>
        <br/>
        Here are the available routes:<br/>
        <br/>  
        Precipitation Analysis:<br/>
        /api/v1.0/precipitation<br/>
        <br/>
        Station Analysis:<br/>
        /api/v1.0/stations<br/>
        <br/>
        Temperture Analysis:<br/>
        /api/v1.0/tobs<br/>
        <br/>
        Start Date Temperture Analysis:<br/>
        /api/v1.0/start<br/>
        <br/>
        Start and End Date Temperture Analysis:<br/>
        /api/v1.0/start/end<br/>
        <br/>''')

###########################################################

# Precipitation route
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
    results = session.query(ST.station, ST.name).all()
     # Convert list of tuples into list of dictionaries for each station and name
    station_list = []
    for result in results:
        r = {}
        r["Station Code"]= result[0]
        r["Station Name"] = result[1]
        station_list.append(r)
    
    # jsonify the list
    return jsonify(station_list)

# creat TOBs route
@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of temperature observations for the previous year"""
    query_date = dt.date(2017,8,23) - dt.timedelta(days=365)
    results = session.query(MS.tobs, MS.date).\
        filter(MS.date >= query_date).all()
    
    # convert list of tuples to show dates and temps
    tobs_list = []
    for result in results:
        r = {}
        r["Date"] = result[1]
        r["Recorded Temp"] = result[0]
        tobs_list.append(r)
    return jsonify(tobs_list = tobs_list)
 
@app.route("/api/v1.0/<start>")
#@app.route("/api/v1.0/<start>/<end>")
def start (start=None, end=None):
    
    """Return a JSON list of tmin, tmax, tavg for the dates greater than or equal to the date provided"""
    
    # Convert start and end dates to yyyy-mm-dd format for the query
    start_dt = dt.datetime.strptime(start, '%Y-%m-%d')
    #end_dt = dt.datetime.strptime(end, '%Y-%m-%d')
    
    if not end:
        results = session.query(MS.date, func.min(MS.tobs), func.avg(MS.tobs),
        func.max(MS.tobs)).filter(MS.date >= start_dt).all()
    # if end:
    #     results = session.query(MS.date, func.min(MS.tobs), func.avg(MS.tobs),
    #     func.max(MS.tobs)).filter(MS.date >= start).filter(MS.date <= end_dt).all()
    
    # Create a list to hold results
    temp_list = []
    for result in results:
        r = {}
        r["Actual Date"] = result[0]
        r["Temp Min"] = result[1]
        r["Temp Avg"] = result[2]
        r["Temp Max"] = result[3]
        temp_list.append(r)
    return jsonify(temp_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start=None, end=None):

    """Return a JSON list of tmin, tmax, tavg for the dates in range of start date and end date inclusive"""
    
    # take start and end dates and convert to yyyy-mm-dd format for the query
    start_dt = dt.datetime.strptime(start, '%Y-%m-%d')
    end_dt = dt.datetime.strptime(end, "%Y-%m-%d")
    
    results = session.query(MS.date, func.min(MS.tobs), func.avg(MS.tobs),func.max(MS.tobs)).filter(MS.date <= end).filter(MS.date >= start).group_by(MS.date).all()
    
    # Create a list to hold results
    temp_list = []
    for result in results:
        r = {}
        r["Actual Date"] = result[0]
        r["Temp Min"] = result[1]
        r["Temp Avg"] = result[2]
        r["Temp Max"] = result[3]
        temp_list.append(r)
    return jsonify(temp_list)

# Close Session
session.close()

if __name__ == "__main__":
    app.run()