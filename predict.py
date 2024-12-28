import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load your data
data = pd.read_csv('static/data/ph_dengue_cases2016-2020.csv')

# Preprocess the data
data['Months'] = data['Months'].astype('category').cat.codes
data['Region'] = data['Region'].astype('category').cat.codes

# Define features and target
X = data[['Months', 'Year', 'Region']]
y_cases = data['Dengue_Cases']
y_deaths = data['Dengue_Deaths']

# Split the data into training and testing sets
X_train, X_test, y_cases_train, y_cases_test = train_test_split(X, y_cases, test_size=0.2, random_state=42)
_, _, y_deaths_train, y_deaths_test = train_test_split(X, y_deaths, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train and evaluate the model for Dengue Cases
model.fit(X_train, y_cases_train)
y_cases_pred = model.predict(X_test)
cases_mse = mean_squared_error(y_cases_test, y_cases_pred)
print(f'Mean Squared Error for Dengue Cases: {cases_mse}')

# Train and evaluate the model for Dengue Deaths
model.fit(X_train, y_deaths_train)
y_deaths_pred = model.predict(X_test)
deaths_mse = mean_squared_error(y_deaths_test, y_deaths_pred)
print(f'Mean Squared Error for Dengue Deaths: {deaths_mse}')
