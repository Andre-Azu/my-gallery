from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse("Hello you! this is your gallery :)")