from django.conf.urls import include, url
from django.contrib import admin
from booktest import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^delete(\d+)$', views.delete),
    url(r'^create$', views.create),
    url(r'^area', views.area),
]
