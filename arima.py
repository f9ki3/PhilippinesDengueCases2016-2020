import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load the dataset
data_path = 'static/data/ph_dengue_cases2016-2020.csv'
df = pd.read_csv(data_path)

# Combine 'Months' and 'Year' into a single datetime column
df['date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Months'].astype(str) + '-01')

# Set the date column as the index
df.set_index('date', inplace=True)

# Group by date and sum the cases and deaths (if there are multiple regions)
df = df.groupby('date').sum()

# Check for missing values
df = df.dropna()

# Fit the ARIMA model for Dengue Cases
model_cases = ARIMA(df['Dengue_Cases'], order=(5, 1, 0))
model_cases_fit = model_cases.fit()

# Print the summary statistics for Dengue Cases model
print("ARIMA Model Summary for Dengue Cases:")
print(model_cases_fit.summary())

# Fit the ARIMA model for Dengue Deaths
model_deaths = ARIMA(df['Dengue_Deaths'], order=(5, 1, 0))
model_deaths_fit = model_deaths.fit()

# Print the summary statistics for Dengue Deaths model
print("ARIMA Model Summary for Dengue Deaths:")
print(model_deaths_fit.summary())

# Make predictions
forecast_cases = model_cases_fit.forecast(steps=12)
forecast_deaths = model_deaths_fit.forecast(steps=12)

# Print the forecasted values
print("Forecasted Dengue Cases for the next 12 months:")
print(forecast_cases)
print("Forecasted Dengue Deaths for the next 12 months:")
print(forecast_deaths)

# Calculate the percentage of deaths
percentage_deaths = (forecast_deaths / forecast_cases) * 100

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(df['Dengue_Cases'], label='Historical Dengue Cases')
plt.plot(forecast_cases, label='Forecast Dengue Cases', color='red')
plt.xlabel('Date')
plt.ylabel('Dengue Cases')
plt.title('Dengue Cases Forecast')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['Dengue_Deaths'], label='Historical Dengue Deaths')
plt.plot(forecast_deaths, label='Forecast Dengue Deaths', color='red')
plt.xlabel('Date')
plt.ylabel('Dengue Deaths')
plt.title('Dengue Deaths Forecast')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(percentage_deaths, label='Forecast Percentage of Deaths', color='green')
plt.xlabel('Date')
plt.ylabel('Percentage of Deaths')
plt.title('Forecast Percentage of Deaths')
plt.legend()
plt.show()

# Save the forecast to a CSV file
forecast_cases.to_csv('/Users/mac/Desktop/PhilippinesDengueCases2016-2020/dengue_cases_forecast.csv', header=True)
forecast_deaths.to_csv('/Users/mac/Desktop/PhilippinesDengueCases2016-2020/dengue_deaths_forecast.csv', header=True)
percentage_deaths.to_csv('/Users/mac/Desktop/PhilippinesDengueCases2016-2020/percentage_deaths_forecast.csv', header=True)