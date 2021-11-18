from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#import pandas as pd
from collections import defaultdict
#import gspread
#from gspread_dataframe import set_with_dataframe
from datetime import date

@api_view(['POST', 'GET'])
def suscripcion(request):
    url = 'https://tarea4taller.herokuapp.com/'
    body = {"url": url}
    body = json.dumps(body)
    r = requests.post(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-4-notifications/subscriptions/26425', headers={"Content-type": "application/json"}, data = body)
    r = r.json()
    return Response(r, status=status.HTTP_200_OK)

@api_view(['DELETE', 'GET'])
def eliminar_sus(request):
    r = requests.delete(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-4-notifications/subscriptions/26425')
    return Response(r, status=status.HTTP_200_OK)


def index(request):
    return HttpResponse("HOLAAA.")
# Create your views here.
