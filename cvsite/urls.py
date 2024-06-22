from django.urls import path 
from cvsite.views import *

app_name = "cvsite"

urlpatterns = [
    path('', home_page, name="index"),
]