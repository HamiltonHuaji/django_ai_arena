from django.urls import path
from . import views

urlpatterns = [
    path('billboard/', views.billboard),
]
