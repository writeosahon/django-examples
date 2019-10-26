from django import http
import datetime
import django.utils.timezone as djangotimezone


# method is used to set the app namespace for the session object used by the app
def set_session_app_namespace(session):
    if not "utopiasoftware-electionsapp" in session: # if the session namespace has not been set
        session.cycle_key() # refresh the session key without destroying session data (prevents unintended page caching)
        session["utopiasoftware-electionsapp"] = {} # set it
        session.modified = True # flag that the session has been modified
    return session # return the session

# error handler/view for 404 on the site
def handler404(request, exception=None):
    with djangotimezone.override("Africa/Lagos"): # use the user's timezone context
        return http.HttpResponse("Sorry, the page you asked for was not found", status=404)