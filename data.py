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


    def getYear(self):
        with open("static/data/ph_dengue_cases2016-2020.csv", mode="r") as files:
            #lets read the file from csv data inside static directory
            reader = csv.reader(files)
            next(reader)

            #we create variable year and set into set() this prevent to duplicate data
            years = set()

            for year in reader:
                #lets add first column or index 0 to the years variable
                years.add(year[1])
            
            nYears = list(years)
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
