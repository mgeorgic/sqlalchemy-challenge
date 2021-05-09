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
        f"Precipitation data:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"Stations:<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"Temperture observations:<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"/api/v1.0/start<br/>"
        f"<br/>"
        f"/api/v1.0/start/end<br/>"
        f"<br/>"
    )
###########################################################

# create precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Retrieve the last 12 months of precipitation data and return the results."""
    # Create the session link
    session = Session(engine)
    
    # Query for the date and precipitation for the last year
    precipitation = session.query(MS, MS.prcp).\
        filter(MS.date >= date).all()

python app.py