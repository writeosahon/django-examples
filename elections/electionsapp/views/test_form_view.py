import django.shortcuts

from django import http
import datetime
import django.utils.timezone as djangotimezone

from django.views.decorators import http as viewdecorators
from ..forms import test_form

# Create your views here.
@viewdecorators.require_http_methods(["GET", "POST"]) # this method can only be accessed via GET
def test_form_view(request):
    if request.method == "POST": # view was requested via "POST" method
        testform = test_form.TestForm(request.POST) # create a bound form using the post data
        if testform.is_valid(): # check if the form is valid
            # do stuff with the valid data
            pass
    else: # view was requested via "GET" method
        # instantiate the Form to be used by the view
        testform = test_form.TestForm()
    # create the context for the form    
    context = {"form": testform}
    # render the form using the specified template and context
    return django.shortcuts.render(request, "electionsapp/testform.html", context)