import csv

class dataSets():
    def getDengue(self, year=None, loc=None):
        # Open the CSV file in read mode
        with open("static/data/doh-epi-dengue-data-2016-2021 (Region-4-A).csv", mode="r") as file:
            # Read the file using csv.reader
            reader = csv.reader(file)

            # Skip the header row
            headers = next(reader)

            # Extract the relevant data by index
            data = []
            for row in reader:
                record = {
                    "loc": row[0].strip(),    # Location is in the first column (index 0)
                    "cases": int(row[1].strip()),  # Cases are in the second column (index 1)
                    "deaths": int(row[2].strip()), # Deaths are in the third column (index 2)
                    "date": self.correct_date_format(row[3].strip()),   # Date is in the fourth column (index 3)
                    "region": row[4].strip()  # Region is in the fifth column (index 4)
                }
                data.append(record)

        # Filter by year if provided
        if year:
            data = [record for record in data if record["date"].split('/')[-1] == str(year)]

        # Filter by location if provided
        if loc:
            data = [record for record in data if record["loc"].lower() == loc.lower()]

        # Sum cases and deaths by year if no specific year or location is provided
        if not year and not loc:
            summary = {}
            for record in data:
                record_year = record["date"].split('/')[-1]
                if record_year not in summary:
                    summary[record_year] = {"cases": 0, "deaths": 0}
                summary[record_year]["cases"] += record["cases"]
                summary[record_year]["deaths"] += record["deaths"]

            # Convert the summary to the required JSON format
            response = {
                "ph_dengue": {
                    "cases_series": [summary[year]["cases"] for year in summary],
                    "deaths_series": [summary[year]["deaths"] for year in summary],
                    "year_series": list(summary.keys())
                }
            }
        elif year:
            # Sum cases and deaths by month if year is provided
            summary = {}
            for record in data:
                record_month = record["date"].split('/')[0]
                if record_month not in summary:
                    summary[record_month] = {"cases": 0, "deaths": 0}
                summary[record_month]["cases"] += record["cases"]
                summary[record_month]["deaths"] += record["deaths"]

            # Convert the summary to the required JSON format
            response = {
                "ph_dengue": {
                    "cases_series": [summary[month]["cases"] for month in summary],
                    "deaths_series": [summary[month]["deaths"] for month in summary],
                    "month_series": list(summary.keys())
                }
            }
        elif loc:
            # Sum cases and deaths by month if location is provided
            summary = {}
            for record in data:
                record_month = record["date"].split('/')[0]
                if record_month not in summary:
                    summary[record_month] = {"cases": 0, "deaths": 0}
                summary[record_month]["cases"] += record["cases"]
                summary[record_month]["deaths"] += record["deaths"]

            # Convert the summary to the required JSON format
            response = {
                "ph_dengue": {
                    "cases_series": [summary[month]["cases"] for month in summary],
                    "deaths_series": [summary[month]["deaths"] for month in summary],
                    "month_series": list(summary.keys())
                }
            }
        else:
            # Sort data by date and location
            sorted_data = sorted(data, key=lambda x: (x["date"], x["loc"]))

            # Convert the sorted data to the required JSON format
            response = {"ph_dengue": sorted_data}

        return response

    def correct_date_format(self, date_str):
        parts = date_str.split('/')
        if len(parts[0]) == 1:
            parts[0] = '0' + parts[0]
        if len(parts[1]) == 1:
            parts[1] = '0' + parts[1]
        return '/'.join(parts)
    
    def getDengueCasesDeath(self, year=None, loc=None):
        # Open the CSV file in read mode
        with open("static/data/doh-epi-dengue-data-2016-2021 (Region-4-A).csv", mode="r") as file:
            # Read the file using csv.reader
            reader = csv.reader(file)

            # Skip the header row
            headers = next(reader)

            # Extract the relevant data by index
            data = []
            for row in reader:
                record = {
                    "loc": row[0].strip(),    # Location is in the first column (index 0)
                    "cases": int(row[1].strip()),  # Cases are in the second column (index 1)
                    "deaths": int(row[2].strip()), # Deaths are in the third column (index 2)
                    "date": self.correct_date_format(row[3].strip()),   # Date is in the fourth column (index 3)
                    "region": row[4].strip()  # Region is in the fifth column (index 4)
                }
                data.append(record)

        # Filter by year if provided
        if year:
            data = [record for record in data if record["date"].split('/')[-1] == str(year)]

        # Filter by location if provided
        if loc:
            data = [record for record in data if record["loc"].lower() == loc.lower()]

        # Sum cases and deaths
        total_cases = sum(record["cases"] for record in data)
        total_deaths = sum(record["deaths"] for record in data)
        response = {"ph_dengue": {"total_cases": total_cases, "total_deaths": total_deaths}}

        return response
    
    def getDengueMostLeastCases(self, year=None, loc=None):
        # Open the CSV file in read mode
        with open("static/data/doh-epi-dengue-data-2016-2021 (Region-4-A).csv", mode="r") as file:
            # Read the file using csv.reader
            reader = csv.reader(file)

            # Skip the header row
            headers = next(reader)

            # Extract the relevant data by index
            data = []
            for row in reader:
                record = {
                    "loc": row[0].strip(),    # Location is in the first column (index 0)
                    "cases": int(row[1].strip()),  # Cases are in the second column (index 1)
                    "deaths": int(row[2].strip()), # Deaths are in the third column (index 2)
                    "date": self.correct_date_format(row[3].strip()),   # Date is in the fourth column (index 3)
                    "region": row[4].strip()  # Region is in the fifth column (index 4)
                }
                data.append(record)

        # Filter by year if provided
        if year:
            data = [record for record in data if record["date"].split('/')[-1] == str(year)]

        # Filter by location if provided
        if loc:
            data = [record for record in data if record["loc"].lower() == loc.lower()]

        if loc:
            # Find the date with most and least cases for the provided location
            if data:
                most_cases_record = max(data, key=lambda x: x["cases"])
                least_cases_record = min(data, key=lambda x: x["cases"])

                response = {
                    "most_cases": {
                    "loc": most_cases_record["loc"],
                    "date": most_cases_record["date"],
                    "cases": most_cases_record["cases"],
                    "deaths": most_cases_record["deaths"]
                    },
                    "least_cases": {
                    "loc": least_cases_record["loc"],
                    "date": least_cases_record["date"],
                    "cases": least_cases_record["cases"],
                    "deaths": least_cases_record["deaths"]
                    }
                }
            else:
                response = {"most_cases": None, "least_cases": None}
        else:
            # Aggregate cases and deaths by location
            summary = {}
            for record in data:
                if record["loc"] not in summary:
                    summary[record["loc"]] = {"cases": 0, "deaths": 0}
                summary[record["loc"]]["cases"] += record["cases"]
                summary[record["loc"]]["deaths"] += record["deaths"]

            # Find the location with most and least cases
            if summary:
                most_cases = max(summary.items(), key=lambda x: x[1]["cases"])
                least_cases = min(summary.items(), key=lambda x: x[1]["cases"])

                response = {
                    "most_cases": {
                        "loc": most_cases[0],
                        "cases": most_cases[1]["cases"],
                        "deaths": most_cases[1]["deaths"]
                    },
                    "least_cases": {
                        "loc": least_cases[0],
                        "cases": least_cases[1]["cases"],
                        "deaths": least_cases[1]["deaths"]
                    }
                }
            else:
                response = {"most_cases": None, "least_cases": None}

        return response


    def getYear(self):
        with open("static/data/doh-epi-dengue-data-2016-2021 (Region-4-A).csv", mode="r") as files:
            # Read the file from CSV data inside the static directory
            reader = csv.reader(files)
            next(reader)

            # Create a variable to store years as a set to prevent duplicates
            years = set()

            for row in reader:
                # Add the year (extracted from the date column index 3) to the set
                date = row[3].strip()
                year = date.split('/')[-1]
                years.add(year)
            
            # Convert the set to a sorted list in ascending order
            nYears = sorted(list(years))
            nnYears = {
                'years': nYears
            }

            return nnYears
    
    def getLocations(self):
        with open("static/data/doh-epi-dengue-data-2016-2021 (Region-4-A).csv", mode="r") as files:
            # Read the file from CSV data inside the static directory
            reader = csv.reader(files)
            next(reader)

            # Create a variable to store locations as a set to prevent duplicates
            locations = set()

            for row in reader:
                # Add the location (column index 0) to the set
                locations.add(row[0].strip())
            
            # Convert the set to a sorted list
            nLocations = sorted(list(locations))
            nnLocations = {
                'locations': nLocations
            }

            return nnLocations


if __name__ == "__main__":
    dataSets().getYear()  
