from django.contrib import admin
from .models import Menuname
from .models import MenuCategory
from .models import Customer
# from .models import Logger_New
# Register your models here.
admin.site.register(Menuname)
admin.site.register(MenuCategory)
admin.site.register(Customer)
# admin.site.register(Logger_New)