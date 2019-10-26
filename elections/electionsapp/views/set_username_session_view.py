import django.shortcuts

from django import http
import datetime
import django.utils.timezone as djangotimezone

from django.views.decorators import http as viewdecorators
from . import set_session_app_namespace

# Create your views here.
@viewdecorators.require_http_methods(["POST", "GET"]) # this method can only be accessed via GET, POST
def set_session(request):
    # call the function to create the namespace for the app with the session object
    set_session_app_namespace(request.session)
    # get the username parameter from the POST or GET parameters submitted
    if request.method == "POST": # data was sent via POST
        username = request.POST.get("username", "writeosahon") # get the posted data or a default value
    elif request.method == "GET": # data was sent via GET
        username = request.GET.get("username", "writeosahon") # get the sent data or a default value
    # set the provided username parameter in session        
    request.session["utopiasoftware-electionsapp"]["username"] = username
    request.session.modified = True # flag that the session has been modified

    # redirect the user to the view where the username stored in session will be displayed
    return django.shortcuts.redirect("electionsapp:greetuser")
    