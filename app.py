from flask import Flask, render_template, jsonify, request
from data import dataSets


app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template("dashboard.html")

# api end points
@app.route('/get_years')
def getYears():
    data = dataSets().getYear()
    return jsonify(data)

@app.route('/get_regions')
def getRegions():
    data = dataSets().getRegion()
    return jsonify(data)

@app.route('/get_dengue')
def getDengueData():
    # Get the filter parameters from the query string
    year = request.args.get('year', default=None, type=int)
    region = request.args.get('region', default=None, type=str)

    # Use the parameters in your data fetching function
    data = dataSets().getDengue(year, region)

    return jsonify(data)

@app.route('/get_dengue_cases_death')
def getDengueDataCasesDeath():
    # Get the filter parameters from the query string
    year = request.args.get('year', default=None, type=int)
    region = request.args.get('region', default=None, type=str)

    # Use the parameters in your data fetching function
    data = dataSets().getDengueCasesDeath(year, region)

    return jsonify(data)

@app.route('/get_dengue_most_least')
def getDengueMostLeastCases():
    # Get the filter parameters from the query string
    year = request.args.get('year', default=None, type=int)
    region = request.args.get('region', default=None, type=str)

    # Use the parameters in your data fetching function
    data = dataSets().getDengueMostLeastCases(year, region)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")