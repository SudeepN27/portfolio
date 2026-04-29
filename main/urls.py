from django.urls import path
from . import views

urlpatterns = [
       path('', views.home),
       path('projects/', views.projects),
       path('contacts/', views.contact),
       path('about/', views.about),
       ]
