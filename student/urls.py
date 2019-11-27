from django.urls import path, include
from django.views.decorators.cache import never_cache
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='home'),
]
