from django.shortcuts import render

from django import http
import datetime
import django.utils.timezone as djangotimezone

from django.views.decorators import http as viewdecorators

# Create your views here.

@viewdecorators.require_GET # this method can only be accessed via GET
def displaytime(request):
    with djangotimezone.override("Africa/Lagos"): # use the user's timezone context
        return http.HttpResponse(djangotimezone.get_current_timezone_name() + 
                            " " + djangotimezone.localtime().strftime('%c %Z'))