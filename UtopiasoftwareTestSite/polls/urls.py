""" File holds the url patterns for the polls app """

from django import urls

from . import views

urlpatterns = [
    urls.path("", view=views.index, name="index"),
    urls.path("index", view=views.index)
]