from flask import Flask, render_template, jsonify
from data import *


app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template("dashboard.html")


# api end points
@app.route('/get_years')
def getYears():
    data = dataSets().getYear()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")