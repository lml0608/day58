# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from django import forms
from django.forms import fields

class UserForm(forms.Form):

    username = fields.CharField(max_length=15)
    email = fields.EmailField()



