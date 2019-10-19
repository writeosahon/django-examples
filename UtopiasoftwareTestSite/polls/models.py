from django.db import models



# Create your models here.

# model for the question table
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        model_dict = {}
        model_dict["question_text"] = self.question_text
        model_dict["pub_date"] = self.pub_date
        return str(self.id) + ": " + self.question_text

#model for the choice table
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        model_dict = {}
        model_dict["choice_text"] = self.choice_text
        model_dict["votes"] = self.votes
        return str(self.id) + ": " + self.choice_text