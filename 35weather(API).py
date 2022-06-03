import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "8b48ca41c2e824b85f6c3f316517d8dd"   #os.environ.get("OWM_API_KEY")
account_sid = "ACce91aca00847b6b8e196478f5a15c2e3"
auth_token = "049db511cea0339b7b12b1029a70e359" #os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": "78.777100",
    "lon": "30.222401",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's sunny today. dont bring an ☔️",
        from_="+19785103059",
        to="+918494020340"
    )
    print(message.status)
