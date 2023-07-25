from django.urls import path
from app3.views import *
app_name='app3'
urlpatterns=[
    path('fifth/', fifth, name='fifth'),
    path('six/', six, name='six'),
    path('string/', string, name='string'),
]