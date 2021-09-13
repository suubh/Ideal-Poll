from django.urls import path, include
from django.contrib import admin


#Creating URL routes 

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls)
]