from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projeler', views.projects, name='project'),
    path('ozgecmis', views.resume, name='resume'),
]