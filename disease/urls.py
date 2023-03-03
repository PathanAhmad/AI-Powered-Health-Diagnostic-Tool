from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^datasets$', views.datasets, name="datasets"),
    re_path(r'^analysis', views.analysis, name="analysis"),
    re_path(r'^all', views.getDisease, name="getDisease"),
    re_path(r'^prediction', views.prediction, name="prediction"),
]
