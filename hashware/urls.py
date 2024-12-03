"""
URL configuration for hashware project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from file import views

urlpatterns = [
    # path('', include('file.urls')),
    path('admin/', admin.site.urls),
    path('file/templates/', admin.site.urls),
    # path('', include('file.urls')),
    path('admin/', admin.site.urls),
    path('file/templates/', admin.site.urls),
    path('file/', views.login),
    path('file/registers.html',views.user_input_view),
    path('file/home.html',views.members),
    path('file/table.html',views.table), 
    path('file/malhome.html',views.malhome),
    path('file/navbar.html',views.navbar),
    path('file/style.css',views.style),
    path('file/hashs.html',views.hash), 
    path('file/logins.html',views.login),
    path('static/back.jpg',views.back),
    path('file/learnlaugh.html',views.learn),
    path('static/back.jpg',views.back),
    path('file/Akshada.html',views.akshada),
    path('file/FeedBack.html',views.feed),
    path('file/mohan.html',views.mohan),
]
