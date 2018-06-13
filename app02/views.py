from django.shortcuts import render,HttpResponse,redirect

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
        print(type(obj))

        if obj.is_valid():

            # UserInfo.objects.create(
            #     username=obj.cleaned_data['user'],
            #     email=obj.cleaned_data['email']
            # )

            UserInfo.objects.create(**obj.cleaned_data)


            return redirect('/app02/users/')

        else:
            return render(request,'add_user.html',{'obj':obj})





def edit_user(request,nid):

    if request.method == "GET":


        userinfo = UserInfo.objects.filter(id=nid).first()

        obj = UserForm({'username':userinfo.username,'email':userinfo.email})

        return render(request,'edit_user.html',{'obj':obj,'nid':nid})

    else:

        obj = UserForm(request.POST)

        if obj.is_valid():

            # UserInfo.objects.create(
            #     username=obj.cleaned_data['user'],
            #     email=obj.cleaned_data['email']
            # )

            UserInfo.objects.filter(id=nid).update(**obj.cleaned_data)

            return redirect('/app02/users/')

        else:
            return render(request, 'edit_user.html', {'obj': obj,'nid':nid})


from django import forms
from django.forms import fields,widgets
class TestForm(forms.Form):

    user = fields.CharField(
        required=True,
        max_length=12,
        min_length=3,
        error_messages={
            #
            # 'required':"",
            # "max_length":"",
            # "min_length":""
        },
        widget= widgets.Textarea()

    )

    age = fields.IntegerField()

    email = fields.EmailField()

def test(request):

    obj = TestForm()
    return render(request,'test.html',{'obj':obj})


class AjaxForm(forms.Form):
    price = fields.IntegerField(max_value=15)
    user_id = fields.IntegerField(

        widget=widgets.Select(choices=[(0,'alex'),(1,'liubin'),(2,'liuxin')])
    )


def ajax(request):

    if request.method == "GET":

        obj = AjaxForm()

        return render(request,'ajax.html',{'obj':obj})

    else:

        ret = {'status':'true','messages':None}
        import json
        obj = AjaxForm(request.POST)

        if obj.is_valid():

            print(obj.cleaned_data)

            return HttpResponse(json.dumps(ret))
        else:

            print(type(obj.errors)) #<class 'django.forms.utils.ErrorDict'>


            ret['status'] = 'false'
            ret['messages'] = obj.errors

            return HttpResponse(json.dumps(ret))



