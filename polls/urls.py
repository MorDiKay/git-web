from django.urls import path
from . import views

urlpatterns = [
    path('', views.change_color),
]