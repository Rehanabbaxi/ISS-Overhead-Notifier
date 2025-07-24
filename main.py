import time
import requests
from datetime import datetime
import smtplib


MY_LAT = 51.507351
MY_LONG = -0.127758
Email = "rehan020344@gmail.com"
Password = "majj upjc ryjf wvsb"

def send_notification():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=Email, password=Password)
        connection.sendmail(from_addr=Email,
                            to_addrs="rehan020344@yahoo.com",
                            msg="Subjet:Look Up \n\nLook Iss Satellite is above you in sky")


def iss_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (iss_latitude - 5 <= MY_LAT >= iss_latitude + 5) and (iss_longitude - 5 <= MY_LONG >= iss_longitude):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now < sunrise or time_now > sunset : ## Checking if  its dark
        return True


while True:
    time.sleep(60)
    if is_night() and iss_over_head():
        send_notification()
