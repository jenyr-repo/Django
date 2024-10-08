from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home,name="home"),
    path('home/', views.form_view),
    # path('reserve/', views.Logger_view),
]