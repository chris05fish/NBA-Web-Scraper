"""nbaStats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from home import views as home_views
from stats import views as stats_views
from graphs import views as graphs_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home),
    path('join/', home_views.create_account),
    path('login/', home_views.login_user),
    path('logout/', home_views.logout_user),
    path('stats/', stats_views.stats),
    path('graphs/', graphs_views.graphs),
]
