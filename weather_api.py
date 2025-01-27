import requests
import json
import pandas as pd


# Access the website https://open-meteo.com/en/docs and generate historical hourly data on Minais Gerais (lat: -21.72,  long: -45.39) from Jan 1 2022 to Dec 31 2023. Generate data on `temperature`, `relative humidity`, `precipitation`, and `surface pressure`.

r = requests.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure")
         
data = r.json() 


# Use this URL to pull your JSON data programmatically into your Python program, and save this object into the path `data/json`.  

file_path = "data/json/data.json"

with open(file_path, "w") as file:
    json.dump(data, file, indent=4) 


#  Remove all the meta-data from this resultant JSON file and keep only the data that describes the time and the variables listed above. Convert this modified JSON file into a CSV file and save it to the path `data/CSV/`. 

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"],
    "relative humidity": data["hourly"]["relative_humidity_2m"],
    "precipitation": data["hourly"]["precipitation"],
    "surface pressure": data["hourly"]["surface_pressure"]
})

df.to_csv("data/csv/data.csv", index=False)

