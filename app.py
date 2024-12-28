from flask import Flask, render_template, jsonify, request
from data import dataSets
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template("dashboard.html")

# api end points
@app.route('/get_years')
def getYears():
    data = dataSets().getYear()
    return jsonify(data)

@app.route('/get_locations')
def getLocations():
    data = dataSets().getLocations()
    return jsonify(data)

@app.route('/get_dengue')
def getDengueData():
    # Get the filter parameters from the query string
    year = request.args.get('year', default=None, type=int)
    loc = request.args.get('location', default=None, type=str)

    # Use the parameters in your data fetching function
    data = dataSets().getDengue(year, loc)

    return jsonify(data)

@app.route('/get_dengue_cases_death')
def getDengueDataCasesDeath():
    # Get the filter parameters from the query string
    year = request.args.get('year', default=None, type=int)
    location = request.args.get('location', default=None, type=str)

    # Use the parameters in your data fetching function
    data = dataSets().getDengueCasesDeath(year, location)

    return jsonify(data)

@app.route('/get_dengue_most_least')
def getDengueMostLeastCases():
    # Get the filter parameters from the query string
    year = request.args.get('year', default=None, type=int)
    location = request.args.get('location', default=None, type=str)

    # Use the parameters in your data fetching function
    data = dataSets().getDengueMostLeastCases(year, location)

    return jsonify(data)

@app.route('/dengue_forecast', methods=['GET'])
def dengue_forecast():
    # Load the dataset
    data_path = 'static/data/ph_dengue_cases2016-2020.csv'
    df = pd.read_csv(data_path)

    # Combine 'Months' and 'Year' into a single datetime column
    df['date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Months'] + '-01')

    # Group by date and sum the cases and deaths
    df = df.groupby('date')[['Dengue_Cases', 'Dengue_Deaths']].sum()

    # Fit the ARIMA models
    from statsmodels.tsa.arima.model import ARIMA
    cases_model = ARIMA(df['Dengue_Cases'], order=(5, 1, 0)).fit()
    deaths_model = ARIMA(df['Dengue_Deaths'], order=(5, 1, 0)).fit()

    # Forecast for the next 12 months
    forecast_cases = cases_model.forecast(steps=12).tolist()
    forecast_deaths = deaths_model.forecast(steps=12).tolist()

    # Calculate percentage of deaths
    percentage_deaths = [(d / c) * 100 if c > 0 else 0 for c, d in zip(forecast_cases, forecast_deaths)]

    # Prepare the response data
    response = {
        'dates': df.index.strftime('%Y-%m').tolist() + pd.date_range(df.index[-1], periods=13, freq='M')[1:].strftime('%Y-%m').tolist(),
        'historical_cases': df['Dengue_Cases'].tolist(),
        'forecast_cases': forecast_cases,
        'historical_deaths': df['Dengue_Deaths'].tolist(),
        'forecast_deaths': forecast_deaths,
        'percentage_deaths': percentage_deaths
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")