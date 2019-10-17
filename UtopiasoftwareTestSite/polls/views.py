from django.shortcuts import render

from django import http

# Create your views here.

# a view for index
def index(request):
    # return a HttpResponse object
    return http.HttpResponse("Hello World From Django Polls index")

