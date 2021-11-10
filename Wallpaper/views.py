from django.http import HttpResponse
from django.shortcuts import render
import json
import requests

query = "dragons"

def Home(request):
    return render(request,"home.html")


def results(request):
    query = request.GET['query']
    print(query)
    url = '''https://pixabay.com/api/?key=15997342-184cac0d09c1d0fb466cfa9c7&image_type=photo&q=''' + query
    r = requests.get(url)
    jsonObject = json.loads(r.text)

    return render(request,"results.html",{'results':jsonObject['hits']})
