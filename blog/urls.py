from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path("find",views.find,name="find"),
    path('postComment', views.postComment, name="postComment"),
    path('', views.blogHome, name="blogHome"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('<str:slug>', views.blogPost, name="blogPost"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)