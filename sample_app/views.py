from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from sample_app.models import  *

# Create your views here.

#@login_required(login_url='sign_in')
def index(request):
    task=Task.objects.filter(user=request.user)
    all_tasks=Task.objects.filter(user=request.user)
    if request.method=="POST":
        task=request.POST["task"]
        tasks=Task(task=task)
        tasks.user=request.user
        print("user :" , tasks.user)
        tasks.save()

        return render(request,'sample_app/index.html',{
            "all_tasks":all_tasks
        })

    return render(request,'sample_app/index.html',{
        'task':task,
        'name':request.user
    })


def sign_up(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return HttpResponseRedirect(reverse('sign_in'))

    return render(request,'sample_app/sign_up.html')


def sign_in(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'sample_app/sign_in.html', {
                "message": "invalid credentials"})

    return render(request,'sample_app/sign_in.html')

def sign_out(request):
    if request.method=="POST":
        logout(request)
    return render(request,'sample_app/sign_in.html',{
        "message":"you are logged out"
    })

def style(request):
    return render(request,'sample_app/style.html')

def media(request):

    return render(request,'sample_app/media.html',{

    })
