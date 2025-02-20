"""
URL configuration for djangobackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from usuarios import views as userviews
from vendedores import views as vendedoresviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userviews.signup, name='signup'),
    path('home/', userviews.home, name='home'),
    path("vendedores/", vendedoresviews.vendedores, name="vendedores"),
    path("exit/", userviews.exit, name="exit"),
    path("signin/", userviews.signin, name="signin"),
    path("signup/", userviews.signup, name="signup"),
    path("vendedores/create/", vendedoresviews.create_vendedor,
         name="create_vendedor"),
    path('vendedores/<int:vendedor_id>/',
         vendedoresviews.detail_vendedor, name='details_vendedor')
]
