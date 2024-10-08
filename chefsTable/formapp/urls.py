from django.urls import path
from formapp import views

urlpatterns = [
    path('reserve/', views.form_view),
    path('about/', views.about),
    # path('food/', views.food),
    path('menu_by_id/', views.menu_by_id),
]