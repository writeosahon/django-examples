from django import urls

from .views import date_display, set_username_session_view, greet_username_session_view

# app namespace
app_name = "electionsapp" 

# URLConfig for the app
urlpatterns = [
    urls.path("datetime", view=date_display.displaytime, name="displaydatetime"),
    urls.path("setuser", view=set_username_session_view.set_session, name="setuser"),
    urls.path("greetuser", view=greet_username_session_view.session_greetings, name="greetuser"),
]
