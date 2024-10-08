from django.db import models
from django import forms
# Create your models here.

class MenuCategory(models.Model):
        menu_category_name=models.CharField(max_length=200)
class Menuname(models.Model):
        menu_item =models.CharField(max_length=100)
        cuisine =models.CharField(max_length=100)
        price =models.IntegerField(null=False)
        category_id =models.ForeignKey(MenuCategory,on_delete=models.PROTECT,default=None,related_name="category_name")

        def __str__(self) -> str:
                return self.menu_item+':'+self.cuisine
class Customer(models.Model):
        name =models.CharField(max_length=100)
        reservation_day =models.CharField(max_length=100)
        seats =models.IntegerField()
        def __str__(self) -> str:
                return self.name
        

# class Logger_New(models.Model):
#     first_name= models.CharField(max_length=200,null=True)
#     last_name= models.CharField(max_length=200,null=True)
#     time_log=models.TimeField(help_text="Enter the exact time")

class Reservation1(models.Model):
        first_name =models.CharField(max_length=100)
        last_name =models.CharField(max_length=100)
        booking_time =models.DateTimeField(auto_now=True)
        

        def __str__(self) -> str:
                return self.first_name
