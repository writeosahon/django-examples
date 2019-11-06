import django.shortcuts

from django import http
import datetime
import django.utils.timezone as djangotimezone
import django.views

from django.views.decorators import http as viewdecorators
from . import set_session_app_namespace

class FilterView(django.views.View):

    def get(self, request):
        return django.shortcuts.render(request, "electionsapp/filters.html", {"numbers": 12567890})
    