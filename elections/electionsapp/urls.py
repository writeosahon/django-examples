from django import urls

from . import views

# app namespace
app_name = "electionsapp" 

# URLConfig for the app
urlpatterns = [
    urls.path("datetime", view=views.displaytime, name="displaydatetime")
]
