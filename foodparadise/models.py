import datetime

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200 ,blank=True)
    msg = models.CharField(max_length=200 ,blank=True)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)


class Reservation(models.Model):
    name = models.CharField(max_length=200 ,blank=True)
    mbl = models.CharField(max_length=200 ,blank=True)
    email = models.CharField(max_length=200 ,blank=True)
    guests = models.CharField(max_length=200 ,blank=True)
    date = models.CharField(max_length=200 ,blank=True)
    time = models.CharField(max_length=200 ,blank=True)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)


class Menu(models.Model):
    DESSERTS = 'DE'
    BEVERAGES = 'BE'
    FASTFOOD = 'FA'
    DINNER = 'DI'
    MENU_CHOICES = [
        (DESSERTS, 'desserts'),
        (BEVERAGES, 'beverages'),
        (FASTFOOD, 'fastfood'),
        (DINNER, 'dinner'),
    ]
    title = models.CharField(max_length=200 ,blank=True)
    description = models.CharField(max_length=200 ,blank=True)
    image = models.CharField(max_length=200 ,blank=True)
    categary = models.CharField(max_length=4, choices=MENU_CHOICES, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)