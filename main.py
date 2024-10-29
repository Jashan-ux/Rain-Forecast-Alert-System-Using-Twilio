import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient  

account_sid = 'AC29deef957b51xxxxxxxxxxxxxxx'
auth_token ='9071762a6b723xxxxxxxxxxxxxxxxxx'

OWM_Endpoint =  "https://api.openweathermap.org/data/2.5/forecast"
api_key = "6105294bf6460fb9xxxxxxxxxxxx"

weather_params = {
    "lat": 29.962310,
    "lon": 74.694800,
    "appid": api_key,
    "cnt": 4

}

will_rain = False
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data =response.json()

for hour_data in weather_data["list"]:
    condition_code =hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain= True

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}
client = Client(account_sid , auth_token, http_client=proxy_client)
if will_rain:
    message = client.messages.create(
        from_='whatsapp:+14155xxxxxxx',
        body="It's going to rain today.Remember to bring an umbrella ☔",
        to='whatsapp:+91930xxxxx10'
    )
    print(message.sid)
else:
    message = client.messages.create(
        from_='whatsapp:+141xxxxxx6',
        body="Good news! The skies are clear,and no rain is forecasted. Enjoy your day without worries! 🌞",
        to='whatsapp:+9193xxxxxx10'
    )
    print(message.sid)
