from django.urls import path
from .apiviews import *

urlpatterns = [
    path('login/' , LoginView),
    path('register/' , RegisterView)
]