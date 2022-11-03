from django.db import models

# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length = 122)
    college = models.CharField(max_length = 122)
    branch = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 12)
    email = models.EmailField()
    problem = models.TextField()
    date = models.DateField()


class Analyse(models.Model):
    name = models.CharField(max_length = 122)
    college = models.CharField(max_length = 122)
    branch = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 12)
    email = models.EmailField()
    question1 = models.CharField(max_length = 4)
    question2 = models.CharField(max_length = 4)
    question3 = models.CharField(max_length = 4)
    question4 = models.CharField(max_length = 4)
    question5 = models.CharField(max_length = 4)
    question6 = models.CharField(max_length = 4)
    question7 = models.CharField(max_length = 4)
    question8 = models.CharField(max_length = 4)
    question9 = models.CharField(max_length = 4)
    date = models.DateField()
    