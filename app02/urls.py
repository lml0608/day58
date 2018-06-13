# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index$', views.index),

    url(r'^users/$', views.user),
    url(r'^add_user/$', views.add_user),
    url(r'^edit_user-(\d+)/$', views.edit_user),


    url(r'^test/$', views.test),
    url(r'^ajax/$', views.ajax),


]
