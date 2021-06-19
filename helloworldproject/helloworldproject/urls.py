from django.contrib import admin
from django.urls import path
from .views import HelloworldClass, helloworldfuction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfuction),
    path('helloworld2/',HelloworldClass.as_view())
]
