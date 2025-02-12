from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), # call the 'index' function from views.py
]