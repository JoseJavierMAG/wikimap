import requests
import mysql.connector

def get_lati_longi(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    api_key = "AIzaSyB_p-4861AKu51TKWKRELGObg4NxZQq1_Q"
    params = {

        "address": address,

        "key": api_key

    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        if data["status"] == "OK":

            location = data["results"][0]["geometry"]["location"]

            lat = location["lat"]

            lng = location["lng"]

            return lat, lng

        else:

            print(f"Error: {data['error_message']}")

            return 0, 0

    else:

        print("Failed to make the request.")

        return 0, 0



address = 'Alcantarilla, Murcia, Spain'

lati, longi = get_lati_longi(address)

print(f"Latitude: {lati}")

print(f"Longitude: {longi}")