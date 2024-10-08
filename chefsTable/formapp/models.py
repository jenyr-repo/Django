from django.db import models
from django import forms
# Create your models here.

class Reserve(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    time_log=models.TimeField(help_text="Enter the exact time")

class Reservation(models.Model):
    name= models.CharField(max_length=100,blank=True)
    contact= models.CharField('Phone_number',max_length=300)
    time=models.TimeField()
    count=models.IntegerField()
    notes=models.CharField(max_length=300,blank=True)

class food(models.Model):
    name= models.CharField(max_length=200)
    price= models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
