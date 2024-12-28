import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import json

def summary_to_dict(summary):
    lines = summary.split('\n')
    summary_dict = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            summary_dict[key.strip()] = value.strip()
    return summary_dict

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

    # Calculate forecast errors for cases
    forecast_cases_errors = model_cases_fit.resid

    # Fit ARIMA model for deaths
    model_deaths = ARIMA(monthly_data['deaths'], order=(5, 1, 0))
    model_deaths_fit = model_deaths.fit()

    # Forecast the next 12 months for deaths
    forecast_deaths = model_deaths_fit.forecast(steps=12)
    forecast_deaths_index = pd.date_range(start=monthly_data.index[-1] + pd.DateOffset(months=1), periods=12, freq='M')

    # Calculate forecast errors for deaths
    forecast_deaths_errors = model_deaths_fit.resid

    # Prepare the JSON output
    forecast_data = {
        "cases": forecast_cases.tolist(),
        "deaths": forecast_deaths.tolist(),
        "month": [date.month for date in forecast_cases_index],
        "year": [date.year for date in forecast_cases_index],
        "model_fit_cases": summary_to_dict(model_cases_fit.summary().as_text()),
        "model_fit_deaths": summary_to_dict(model_deaths_fit.summary().as_text()),
        "forecast_errors_cases": forecast_cases_errors.tolist(),
        "forecast_errors_deaths": forecast_deaths_errors.tolist()
    }

    return forecast_data
