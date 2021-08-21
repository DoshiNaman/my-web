from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
   path("find",views.find,name="find"),
   path("",views.index,name="home"),
   path("cv/",views.cv,name="cv"),
   #path('search/', views.search, name="search"),
]