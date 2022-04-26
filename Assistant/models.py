from enum import auto
from pyexpat import model
from django.db import models
from django.forms import CharField, DateField
from js2py import require

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=75)
    email = models.EmailField(max_length=50)
    designation = models.CharField(max_length=75)
    specialization = models.TextField()
    achivements = models.TextField()

class Event(models.Model):
    ename = models.CharField(max_length=75)
    eorganizers = models.CharField(max_length=50)
    ediscription = models.TextField()
    ecoordinators = models.TextField()

class Notice(models.Model):
    date = models.DateField()
    notice = models.TextField()

class calendardetails(models.Model):
    month = models.CharField(max_length=20)
    date = models.DateField()
    purpose = models.TextField()
    






