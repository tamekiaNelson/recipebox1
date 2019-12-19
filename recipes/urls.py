"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from recipes import views
from recipes.models import Author, Recipe


admin.site.register(Author)
admin.site.register(Recipe)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('recipe/<int:id>/', views.recipe, name='recipes'),
    path('author/<int:id>/', views.author, name='authors'),
    path('authoradd/', views.authoraddview, name='authoradd'),
    path('recipeadd/', views.recipeaddview, name='recipeadd'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
