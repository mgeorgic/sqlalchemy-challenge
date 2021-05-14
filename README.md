# sqlalchemy-challenge

SQLAlchemy Challenge

Climate Analysis and Exploration
Using Python, SQLAlchemy, Pandas and Matplotlib

Techniques Demonstrated:

•	Web Site Modeling: used several url’s for user 
•	Data Engineering: used SQLAlchemy ORM queries to show results in webpage url routes
•	Data Analysis: used Pandas and Matplotlib on SQLite Hawaii Weather database

Repository Navigation:
1.	Resources: 2 CSV’s holding the station and measurement data from the SQLite Hawaii database, which was analyzed.
2.	Code: “climate” for data analysis and “app.py” for website SQL ORM queries
3.	Images: contains all graphs created from climate code 


Precipitation Analysis
•	Design a query to retrieve the last 12 months of precipitation data.
•	Select only the date and prcp values.
•	Load the query results into a Pandas DataFrame and set the index to the date column.
•	Sort the DataFrame values by date.
•	Plot the results using the DataFrame plot method.
•	Use Pandas to print the summary statistics for the precipitation data.

Station Analysis
•	Design a query to calculate the total number of stations.
•	Design a query to find the most active stations.
o	List the stations and observation counts in descending order.
o	Which station has the highest number of observations?
•	Design a query to retrieve the last 12 months of temperature observation data (tobs).
o	Filter by the station with the highest number of observations.
o	Plot the results as a histogram with bins=12.

Climate App
Design a Flask API, based on the data queries that was developed.
•	Use FLASK to create the routes.

Flask Routes
•	/
o	Home page.
o	List all routes that are available.
•	/api/v1.0/precipitation
o	Convert the query results to a Dictionary using date as the key and prcp as the value.
o	Return the JSON representation of your dictionary.
•	/api/v1.0/stations
o	Return a JSON list of stations from the dataset.
•	/api/v1.0/tobs
o	query for the dates and temperature observations from a year from the last data point.
o	Return a JSON list of Temperature Observations (tobs) for the previous year.
•	/api/v1.0/<start> and /api/v1.0/<start>/<end>
o	Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
o	When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
o	When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

Temperature Analysis I
•	Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
•	You may either use SQLAlchemy or pandas's read_csv() to perform this portion.
•	Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.
•	Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

Temperature Analysis II
•	Use the calc_temps function to calculate the min, avg, and max temperatures for the dates using the matching dates from the previous year (i.e., use "2017-01-01" if the start date was "2018-01-01").
•	Plot the min, avg, and max temperature from your previous query as a bar chart.
o	Use the average temperature as the bar height.
o	Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr).

Daily Rainfall Average
•	Calculate the rainfall per weather station using the previous year's matching dates.
•	Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.
•	Create a list of dates for your trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list.
•	Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
•	Use Pandas to plot an area plot (stacked=False) for the daily normals.

