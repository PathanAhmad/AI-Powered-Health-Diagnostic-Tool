#from django.conf.urls import re_path
from django.urls import re_path
from . import views

urlpatterns = [
    #url(r'^$', views.index, name="signin"),
    re_path(r'^$', views.index, name="login"),
    re_path(r'^report$', views.user_listing, name="user_listing"),
    re_path(r'^dashboard$', views.dashboard, name="dashboard"),
    re_path(r'^report/(?P<userId>\w{0,50})/$', views.user_listing, name="user_listing"),
    re_path(r'^update/(?P<userId>\w{0,50})/$', views.update, name="update"),
    re_path(r'^add$', views.add, name="add"),
    re_path(r'^forgot$', views.forgot, name="forgot"),
    re_path(r'^logout$', views.logout, name="logout"),
    re_path(r'^changepassword$', views.changepassword, name="changepassword"),
    re_path(r'^delete/(?P<userId>\w{0,50})/$', views.delete, name="delete"),
]