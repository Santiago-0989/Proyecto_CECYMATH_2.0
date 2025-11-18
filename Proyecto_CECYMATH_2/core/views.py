from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(recuest):
    return render(recuest, "core/index.html")
    