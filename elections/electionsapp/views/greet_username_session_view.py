import django.shortcuts

from django import http
import datetime
import django.utils.timezone as djangotimezone

from django.views.decorators import http as viewdecorators
from . import set_session_app_namespace

# Create your views here.
@viewdecorators.require_http_methods(["GET"]) # this method can only be accessed via GET
def session_greetings(request):
    # call the function to create the namespace for the app with the session object
    set_session_app_namespace(request.session)
    # get the username parameter from the POST or GET parameters submitted

    # get the provided session username        
    username = request.session["utopiasoftware-electionsapp"].get("username", None)
    if username is None: # session username has NOT been set
        return http.HttpResponse("Username has not been set")
    else:
        return http.HttpResponse("Hello {}".format(username))
    