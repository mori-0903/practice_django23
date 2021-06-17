from django.contrib import admin
from django.urls import path
from .views import helloworldfuction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfuction),
]
