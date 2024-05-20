from django.urls import path
from .views import *

urlpatterns = [
    path("",home),
    path("register",registerchecker),
    path("select",select), 
    path("delete/<int:id>",delete),
    path("update/<int:id>",update),
    path("login",login),   
]