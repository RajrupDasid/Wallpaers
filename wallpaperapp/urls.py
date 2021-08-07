from django.urls import path
from .views import Index
app_name='wallpaperapp'
urlpatterns=[
    path('',Index,name='index'),
]