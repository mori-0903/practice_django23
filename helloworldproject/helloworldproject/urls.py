from django.contrib import admin
from django.urls import path , include
from .views import HelloworldClass, helloworldfuction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfuction),
    path('helloworld2/',HelloworldClass.as_view()),
    path('app/', include('helloworldapp.urls'))
]
