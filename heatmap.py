import math

def heatmap():
    data = {
        "location": [
            "Batangas",
            "Cavite",
            "Laguna",
            "Lucena City",
            "Quezon",
            "Rizal"
        ],
        "data": [
            float('nan'),
            float('nan'),
            0.6444565192782268,
            float('nan'),
            float('nan'),
            float('nan'),
            float('nan'),
            float('nan'),
            1.0,
            float('nan'),
            float('nan'),
            float('nan'),
            0.9511874844347846,
            float('nan'),
            float('nan'),
            0.059611945029319206,
            float('nan'),
            float('nan'),
            float('nan'),
            float('nan'),
            float('nan'),
            0.4123027462700084,
            float('nan'),
            float('nan'),
            float('nan'),
            float('nan'),
            float('nan'),
            float('nan'),
            float('nan'),
            0.6268197151848581
        ]
    }

    heatmap = {
        "location": data["location"],
        "data": [None if math.isnan(value) else value for value in data["data"]]
    }
    return heatmap
