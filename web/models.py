from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User


# Create your models here.
class KharjHa(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
    def _str_(self):
        return "{}-{}".format(self.text, self.amount)

class Phone(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone_number = models.IntegerField()

class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.text
