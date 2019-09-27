from django.contrib import admin
from django.urls import path
from basic.views import BasicView
from django.conf import settings



urlpatterns = [

    path('', BasicView)
]

