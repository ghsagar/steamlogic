from django.contrib import admin
from django.urls import path
 
from . import views
urlpatterns = [
     
    path('', views.home,name="homepage"),
    path("gallery/",views.gallery, name="gallery"),
    path("about/",views.about, name="about"),
    path("events/",views.events, name="events")
]
