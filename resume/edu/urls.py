from django.urls import path
from .views import *

urlpatterns = [
    path("skills",skills,name="skills")
    ]