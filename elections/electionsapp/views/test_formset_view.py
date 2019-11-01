import django.shortcuts

from django import http
import datetime
import django.utils.timezone as djangotimezone

from django.views.decorators import http as viewdecorators
from ..forms import test_form, test_formset_form

# Create your views here.
@viewdecorators.require_http_methods(["GET", "POST"]) # this method can only be accessed via GET
def test_formset_view(request):
    if request.method == "POST": # view was requested via "POST" method
        testformset = test_formset_form.\
            TestFormSet(request.POST) # create a bound formset using the post data
        if testformset.is_valid(): # check if the formset is valid
            # do stuff with the valid data
            pass
    else: # view was requested via "GET" method
        # instantiate the Formset to be used by the view
        testformset = test_formset_form.TestFormSet()
    # create the context for the formset    
    context = {"formset": testformset}
    # render the formset using the specified template and context
    return django.shortcuts.render(request, "electionsapp/testformset.html", context)