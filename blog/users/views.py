from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

from users.models import UserModel
from users.forms import RegisterForm,LoginForm
# Create your views here.


def register(request):
    request_form=RegisterForm(request.POST)
    if request_form.is_valid():
        post=request.POST
        user_name=post.get('user_name','')
        pass_word1=post.get('pass_word1','')
        pass_word2=post.get('pass_word2','')
        if pass_word1 != pass_word2:
            return render(request,'users/register.html')
        email=post.get('email','')
        users=UserModel()
        users.username=user_name
        users.password=make_password(pass_word2)
        users.email=email
        users.save()
        return render(request,'blog/index.html')
    else:
        return render(request,'users/register.html')


def login_user(request):
    login_form=LoginForm(request.POST)
    if login_form.is_valid():
        post=request.POST
        user_name=post.get('username','')
        pass_word=post.get('password','')
        user=authenticate(username=user_name,password=pass_word)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,'users/register.html')
        else:
            return render(request,'users/register.html')
    else:
        return render(request,'users/register.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))