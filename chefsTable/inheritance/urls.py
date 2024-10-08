from django.urls import path
from inheritance import views

urlpatterns = [
    path('home2/', views.home2),
    path('about2/', views.about2),
    path('menu2/', views.menu2),
]