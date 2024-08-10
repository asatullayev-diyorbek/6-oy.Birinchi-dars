import pprint

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('first-url/', views.first_url, name='first_url'),
    path('second-url/', views.second_url, name='second_url'),
    path('third-url/', views.third_url, name='third_url'),
    path('fourth-url/', views.fourth_url, name='fourth_url'),
    path('fifth-url/', views.fifth_url, name='fifth_url'),
    path('sixth-url/', views.sixth_url, name='sixth_url'),
    path('seventh-url/', views.seventh_url, name='seventh_url'),
    path('eighth-url/', views.eighth_url, name='eighth_url'),
    path('ninth-url/', views.ninth_url, name='ninth_url'),
    path('tenth-url/', views.tenth_url, name='tenth_url')
]
