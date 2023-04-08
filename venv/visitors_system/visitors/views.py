from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import User
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, "login.html",{"user_form":UserCreationForm})

def signup(request):
    if request.method == "POST":
        myform = UserCreationForm(request.POST)
        if myform.is_valid():
            myform.is_superuser = True
            myform.is_stuff = True
            myform.is_stuff = False
            myform.save()
            return render(request, "result.html")
        else:
            return redirect('/')
    else:
        return redirect('/')
