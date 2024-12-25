import csv

class dataSets():
    def getDengue(self, month=None, year=None, region=None):
        # Define the month order for sorting
        month_order = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12
        }

        # Open the CSV file in read mode
        with open("static/data/ph_dengue_cases2016-2020.csv", mode="r") as file:
            # Read the file using csv.reader
            reader = csv.reader(file)

            # Skip the header row
            headers = next(reader)

            # Extract the relevant data by index
            data = []
            for row in reader:
                record = {
                    "month": row[0].strip(),  # Month is in the first column (index 0)
                    "year": row[1].strip(),   # Year is in the second column (index 1)
                    "region": row[2].strip(), # Region is in the third column (index 2)
                    "cases": row[3].strip(),  # Cases are in the fourth column (index 3)
                    "death": row[4].strip()   # Death is in the fifth column (index 4)
                }
                data.append(record)

        # Filter by month if provided
        if month:
            data = [record for record in data if record["month"].lower() == month.lower()]

        # Filter by year if provided
        if year:
            data = [record for record in data if record["year"] == str(year)]

        # Filter by region if provided
        if region:
            data = [record for record in data if record["region"].lower() == region.lower()]

        # Sort data by month and region
        sorted_data = sorted(data, key=lambda x: (month_order[x["month"]], x["region"]))

        # Convert the sorted data to the required JSON format
        response = {"ph_dengue": sorted_data}
        return response
    
    def getDengueCasesDeath(self, year=None, region=None):
        # Open the CSV file in read mode
        with open("static/data/ph_dengue_cases2016-2020.csv", mode="r") as file:
            # Read the file using csv.reader
            reader = csv.reader(file)

            # Skip the header row
            headers = next(reader)

            # Extract the relevant data by index
            data = {}
            for row in reader:
                record_year = row[1].strip()
                record_region = row[2].strip()
                cases = int(row[3].strip())
                death = int(row[4].strip())

                if (record_year, record_region) not in data:
                    data[(record_year, record_region)] = {"cases": 0, "death": 0}

                data[(record_year, record_region)]["cases"] += cases
                data[(record_year, record_region)]["death"] += death

        # Filter by year if provided
        if year:
            data = {k: v for k, v in data.items() if k[0] == str(year)}

        # Filter by region if provided
        if region:
            data = {k: v for k, v in data.items() if k[1].lower() == region.lower()}

        # If no year and region are provided, sum all cases and deaths
        if not year and not region:
            total_cases = sum(v["cases"] for v in data.values())
            total_deaths = sum(v["death"] for v in data.values())
            response = {"ph_dengue": {"total_cases": total_cases, "total_deaths": total_deaths}}
        else:
            # Convert the data to the required JSON format
            sorted_data = [{"cases": v["cases"], "death": v["death"]} for k, v in data.items()]
            response = {"ph_dengue": sorted_data}

        return response
    
    def getDengueMostLeastCases(self, year=None, region=None):
        # Open the CSV file in read mode
        with open("static/data/ph_dengue_cases2016-2020.csv", mode="r") as file:
            # Read the file using csv.reader
            reader = csv.reader(file)

            # Skip the header row
            headers = next(reader)

            # Extract the relevant data by index
            data = {}
            for row in reader:
                record_year = row[1].strip()
                record_region = row[2].strip()
                cases = int(row[3].strip())
                death = int(row[4].strip())

                if (record_year, record_region) not in data:
                    data[(record_year, record_region)] = {"cases": 0, "death": 0}

                data[(record_year, record_region)]["cases"] += cases
                data[(record_year, record_region)]["death"] += death

        # Filter by year if provided
        if year:
            data = {k: v for k, v in data.items() if k[0] == str(year)}

        # Filter by region if provided
        if region:
            data = {k: v for k, v in data.items() if k[1].lower() == region.lower()}

        # Find the region with most and least cases
        if data:
            most_cases = max(data.items(), key=lambda x: x[1]["cases"])
            least_cases = min(data.items(), key=lambda x: x[1]["cases"])

            response = {
                "most_cases": {
                    "year": most_cases[0][0],
                    "region": most_cases[0][1],
                    "cases": most_cases[1]["cases"],
                    "death": most_cases[1]["death"]
                },
                "least_cases": {
                    "year": least_cases[0][0],
                    "region": least_cases[0][1],
                    "cases": least_cases[1]["cases"],
                    "death": least_cases[1]["death"]
                }
            }
        else:
            response = {"most_cases": None, "least_cases": None}

        return response


    def getYear(self):
        with open("static/data/ph_dengue_cases2016-2020.csv", mode="r") as files:
            # Read the file from CSV data inside the static directory
            reader = csv.reader(files)
            next(reader)

            # Create a variable to store years as a set to prevent duplicates
            years = set()

            for year in reader:
                # Add the year (column index 1) to the set
                years.add(year[1])
            
            # Convert the set to a sorted list in descending order
            nYears = sorted(list(years), reverse=False)
            nnYears = {
                'years': nYears
            }

            return nnYears
    
    def getRegion(self):
        with open("static/data/ph_dengue_cases2016-2020.csv", mode="r") as files:
            # Read the file from CSV data inside the static directory
            reader = csv.reader(files)
            next(reader)

            # Create a variable to store regions as a set to prevent duplicates
            regions = set()

            for region in reader:
                # Add the region (column index 2) to the set
                regions.add(region[2])
            
            # Convert the set to a sorted list
            nRegions = sorted(list(regions))
            nnRegions = {
                'regions': nRegions
            }

            return nnRegions


if __name__ == "__main__":
    dataSets().getYear()  
