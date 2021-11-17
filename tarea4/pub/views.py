from django.shortcuts import render
from django.http import HttpResponse
import requests
import pandas as pd
from collections import defaultdict
import gspread
from gspread_dataframe import set_with_dataframe
from datetime import date

paises = ["AUS", "USA", "CHL", "NLD", "IRL", "JPN"]
atributos = ["GHO", "YEAR", "Display", "COUNTRY", "SEX", "GHECAUSES", "AGEGROUP", "Numeric", "Low", "High",
             "Presion arterial", "Glucosa", "Colesterol", "Alcohol", "Cigarros", "Tabaco"]
indicadores = ["Total de operaciones recibidas"]

def suscripcion():
    url = ''
    body = {"url": {url}}
    body = json.dumps(body)
    r = requests.post(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-4-notifications/subscriptions/{26425}', headers={"Content-type": "application/json"}, data = body)
    return r.json()


def eliminar_sus():
    r = requests.post(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-4-notifications/subscriptions/{26425}')
    return r.json()


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
