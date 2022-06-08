import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

API_ID = "d5935cbf"
# API_ID = os.environ.get("API_ID")
API_KEY = "82960a415f655736b012b31871189cb9"
# API_KEY = os.environ.get("API_KEY")
USERNAME = "hasaanqari9"
# USERNAME = os.environ.get("USERNAME")
PASSWORD = "Iamhassan.9"
# PASSWORD = os.environ.get("PASSWORD")

headers = {
    "x-app-id":API_ID,
    "x-app-key":API_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

data = {
 "query":input("Tell me what exercise you did: "),
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":20,
}

response = requests.post(url=exercise_endpoint,json=data,headers=headers)
data = response.json()
print(data)

sheets_endpoint = "https://api.sheety.co/b082ac113044d5533e1c97206c167efa/myWorkout/workouts"

today = datetime.now()
for exercise in data["exercises"]:
  print(exercise)
  sheet_data = {
      "workout": {
          "date":today.strftime('%d/%m/%Y'),
          "time":today.strftime('%X'),
          "exercise": exercise["name"].title(),
          "duration": exercise["duration_min"],
          "calories": exercise["nf_calories"],
      }
  }

  response2 = requests.post(url=sheets_endpoint,json=sheet_data,auth=(USERNAME,PASSWORD))
  print(response2.text)
  print(response2)
# Ran 5k and cycled for 28 minutes.
