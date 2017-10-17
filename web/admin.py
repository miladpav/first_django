from __future__ import unicode_literals
from django.contrib import admin
from .models import Expense, Phone, Income
from django.utils.encoding import python_2_unicode_compatible
# Register your models here.

admin.site.register(Expense)
admin.site.register(Phone)
admin.site.register(Income)
