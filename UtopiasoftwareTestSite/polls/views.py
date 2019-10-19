from django.shortcuts import render

from django import http
from django import shortcuts
from polls import models

# Create your views here.

# a view for index
def index(request):
    # load all available questions from the data
    all_questions = models.Question.objects.all() 

    # create a context for the template to execute in
    context = {"all_questions_list": all_questions}
    # return a HttpResponse object using the shortcuts render() method
    return shortcuts.render(request, "polls/index.html", context)

    # return a HttpResponse object
    # return http.HttpResponse("Hello World From Django Polls index")

