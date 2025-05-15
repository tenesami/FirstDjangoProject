from django.urls import path
from . import views
# from django.contrib import admin

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
