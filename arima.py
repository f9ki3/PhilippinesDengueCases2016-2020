import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import json

def forecast_dengue():
    file_path = "static/data/doh-epi-dengue-data-2016-2021 (Region-4-A).csv"
    # Load the CSV file
    data = pd.read_csv(file_path)

    # Ensure the 'date' field is in datetime format
    data['date'] = pd.to_datetime(data['date'])

    # Prepare the data for ARIMA model
    monthly_data = data.set_index('date').resample('M').sum()

    # Fit ARIMA model for cases
    model_cases = ARIMA(monthly_data['cases'], order=(5, 1, 0))
    model_cases_fit = model_cases.fit()

    # Forecast the next 12 months for cases
    forecast_cases = model_cases_fit.forecast(steps=12)
    forecast_cases_index = pd.date_range(start=monthly_data.index[-1] + pd.DateOffset(months=1), periods=12, freq='M')

    # Fit ARIMA model for deaths
    model_deaths = ARIMA(monthly_data['deaths'], order=(5, 1, 0))
    model_deaths_fit = model_deaths.fit()

    # Forecast the next 12 months for deaths
    forecast_deaths = model_deaths_fit.forecast(steps=12)
    forecast_deaths_index = pd.date_range(start=monthly_data.index[-1] + pd.DateOffset(months=1), periods=12, freq='M')

    # Prepare the JSON output
    forecast_data = {
        "cases": forecast_cases.tolist(),
        "deaths": forecast_deaths.tolist(),
        "month": [date.month for date in forecast_cases_index],
        "year": [date.year for date in forecast_cases_index]
    }

    return forecast_data
