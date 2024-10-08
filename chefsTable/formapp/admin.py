from django.contrib import admin
from .models import Reserve
from .models import Reservation
from .models import food

# from .models import Logger_New
# Register your models here.
admin.site.register(Reserve)
admin.site.register(Reservation)
admin.site.register(food)

