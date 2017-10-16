from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kharj(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
class Phone(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone_number = models.IntegerField()
