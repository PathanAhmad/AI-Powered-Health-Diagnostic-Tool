from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.listing, name="topics-listing"),
    re_path(r'^list/(?P<id>\w{0,50})/$', views.lists, name="topics-lists"),
    re_path(r'^add$', views.add, name="add"),
    re_path(r'^delete/(?P<id>\w{0,50})/$', views.delete, name="delete"),
    re_path(r'^update/(?P<topicsId>\w{0,50})/$', views.update, name="update"),
]
