from django.urls import path
from . import views

app_name= 'menu'

urlpatterns = [
    path('', views.index,name="index"),
    path('GetPizzas', views.api_get_pizzas),
    
]