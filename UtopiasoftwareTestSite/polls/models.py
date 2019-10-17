from django.db import models

import json


# Create your models here.

# model for the question table
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        model_json = {}
        model_json["question_text"] = self.question_text
        model_json["pub_date"] = self.pub_date
        return json.dumps(model_json)

#model for the choice table
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        model_json = {}
        model_json["choice_text"] = self.choice_text
        model_json["votes"] = self.votes
        return json.dumps(model_json)