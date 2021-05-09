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

# Start session
session = Session(engine)

# Return the lastest date within the database
last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

# Return the date 1 year ago from the lastest date in the database
query_date = dt.date(2017,8,23) - dt.timedelta(days=365)

session.close()

# Create an app
app = Flask(__name__)
