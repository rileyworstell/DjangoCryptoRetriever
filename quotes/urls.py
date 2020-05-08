from django.urls import path
from . import views

#pk_bd922c95c8b845cd8414c2c98eb9f79d

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('topCurrencies', views.topCurrencies, name="topCurrencies"),
]
