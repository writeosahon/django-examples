""" File holds the url patterns for the polls app """

from django import urls

from . import views

app_name = "polls" # the namespace to be used by your templates when referencing url names

urlpatterns = [
    urls.path("", view=views.index, name="index"),
    urls.path("index", view=views.index, name="index")
]