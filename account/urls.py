from django.contrib import admin
from django.urls import path
from .views import sign_up

app_name = 'account'

urlpatterns = [
    path('signup/', sign_up, name='sign_up'),    

]