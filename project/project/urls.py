import pprint

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def a(request):
    pprint.pprint(request.__dict__)
    return HttpResponse("<h1 style='color: red; font-size: 50px;'>Hello, World!</h1>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', a)
]
