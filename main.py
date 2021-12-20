import requests
#hosur
# MY_LAT = 12.728030
# MY_LAN = 77.827057
from twilio.rest import Client

account_sid = "AC41beda6ea70c387627a97a34ccff2a5a"
auth_token = "5971d54be1c2cf58ba2b8c092f54bb26"

 


MY_LAT = 48.427502
MY_LAN = -123.367264

API_KEY = "e6c2ec65e7ed20cd86188d0edfd8157c"
will_rain = False

URL  = 'https://api.openweathermap.org/data/2.5/weather?q=Hosur,in&APPID=e6c2ec65e7ed20cd86188d0edfd8157c'

ONECALL_URL = "https://api.openweathermap.org/data/2.5/onecall"

ONECALL_URL_PARAMS = {
    "lat": MY_LAT,
    "lon": MY_LAN,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(ONECALL_URL,params=ONECALL_URL_PARAMS)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]


for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Its going to rain today, take an umbrella ☂️",
        from_='+16203198098',
        to='+918189804830'
    )

    print(message.status)


