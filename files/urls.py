from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.listing, name="files-listing"),
    re_path(r'^list$', views.lists, name="files-lists"),
    re_path(r'^add$', views.add, name="add"),
    re_path(r'^delete/(?P<id>\w{0,50})/$', views.delete, name="delete"),
]
