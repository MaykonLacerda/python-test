from django.urls import path
from app_cad_users import views

urlpatterns = [
    path('', views.index, name='index'),
]
