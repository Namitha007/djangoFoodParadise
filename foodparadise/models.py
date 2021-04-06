import datetime

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200 ,blank=True)
    msg = models.CharField(max_length=200 ,blank=True)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
