from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("<h2>Understanding Django with python3</h2>")
# Create your views here.
