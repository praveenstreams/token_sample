
from django.contrib import admin
from django.urls import path,include
from tokenapp import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urls),name='urls')
]
