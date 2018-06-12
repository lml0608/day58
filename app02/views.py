from django.shortcuts import render,HttpResponse

# Create your views here.

from .models import *

from .myforms import UserForm


def index(request):

    return HttpResponse("OK")


def user(request):

    user_list = UserInfo.objects.all()

    return render(request,'users.html',{'user_list':user_list})


def add_user(request):

    if request.method =="GET":

        obj = UserForm()

        return render(request,'add_user.html',{'obj':obj})

    else:

        obj = UserForm(request.POST)

        if obj.is_valid():
            print(obj.cleaned_data)

            return HttpResponse("OK")

        else:
            return render(request,'add_user.html',{'obj':obj})






