#pip install requests python-dotenv Flask
#from flask import Flask, render_template
from dotenv import load_dotenv
from pprint import pprint
import requests
import os

#app = Flask(__name__)
#@app.route("/")

load_dotenv()

def get_current_weather(city="Três Lagoas"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    print('\n*** some cool message***\n')
    city = input("\nInsira a cidade:")

    #tratar erros de input
    if not bool(city.strip()):
        city = "Nova Andradina" #input vazio leva, por padrao, pra nova andradina


    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data) 
