from django.urls import path, include
from django.views.decorators.cache import never_cache
from . import views

app_name = 'administrator'

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('form_notice/', views.form_notice, name='form_notice'),
    path('form_dues_stu/', views.form_dues_stu, name='form_dues_stu'),
    path('form_dues_tea/', views.form_dues_tea, name='form_dues_tea'),
    path('form_hos/', views.form_hos, name='form_hos'),
    path('form_stu/', views.form_stu, name='form_stu'),
    path('form_tea/', views.form_tea, name='form_tea'),
]
