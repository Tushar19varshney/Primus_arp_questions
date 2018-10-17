from django.urls import path, include
from .views import *

urlpatterns = [
    path('questions/', Ques.as_view()),
    path('durgesh/', Durgesh.as_view()),
]
