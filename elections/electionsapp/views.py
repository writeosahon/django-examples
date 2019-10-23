from django.shortcuts import render

from django import http
import datetime
import django.utils.timezone as djangotimezone


# Create your views here.

# error handler/view for 404 on the site
def handler404(request, exception=None):
    with djangotimezone.override("Africa/Lagos"): # see the user's timezone context
        return http.HttpResponse("The page you asked for was not found")

def displaytime(request):
    with djangotimezone.override("Africa/Lagos"): # see the user's timezone context
        return http.HttpResponse(djangotimezone.get_current_timezone_name() + 
                            " " + djangotimezone.localtime().strftime('%c %Z'))