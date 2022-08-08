from django.contrib import admin
from django.urls import path,include
from project1 import views

urlpatterns = [
    path('1/',views.ans_form,name="ans")
]