import csv

class dataSets():
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

if __name__ == "__main__":
    dataSets().getYear()  
