from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("About Us in views")