from .views import message 
from django.urls import path 

urlpatterns = [
    path('protected-route/', message) 
]
