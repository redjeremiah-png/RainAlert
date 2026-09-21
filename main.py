
# https://api.openweathermap.org/data/2.5/weather?q=Colorado+Springs&appid=413afede87ffcbdefad327c737ff42ba

import requests

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1551352189572747386/tLwhOI-ZmuYtOhH2vQH2NQsTG2_M1LzB5hEriijGAoQhjmkYgI012yzJNw0K_9x7pqw-"

# To force a lock-screen push notification, include an @everyone or @user mention
# Replace YOUR_DISCORD_USER_ID with your actual numerical Discord ID
USER_ID = "542169621130772520"


def send_sms_alert(sender_name, message_text):
    payload = {
        # Standard plain-text content with a user mention to trigger mobile push
        "content": f"<@{USER_ID}> **{sender_name}:** {message_text}",

        # Override bot name to look like a sender contact
        "username": sender_name,

        # Optional: Custom profile picture URL (e.g., SMS icon)
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/888/888846.png"
    }

    requests.post(WEBHOOK_URL, json=payload)


# Example Usage


LAT = 	39.6876
LONG = 	-104.9103

url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "413afede87ffcbdefad327c737ff42ba"

weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "cnt": 4,
}
will_rain = False
response = requests.get(url=url,params=weather_params)
response.raise_for_status()
weather_data = response.json()
conditions = []
print(weather_data)
conditions.append(weather_data["list"][0]["weather"][0]["id"])
conditions.append(weather_data["list"][1]["weather"][0]["id"])
conditions.append(weather_data["list"][2]["weather"][0]["id"])
conditions.append(weather_data["list"][3]["weather"][0]["id"])
for item in conditions:
    print(item)
    if item < 800:
        will_rain = True
if will_rain:
    send_sms_alert("Rain Indicator", "It is going to Rain!")



