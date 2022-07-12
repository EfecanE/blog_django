from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login as login_process
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_process
from django.contrib import messages

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login_process(request,newUser)
        messages.success(request, "Your profile was created successfully.")

        return redirect("index")
    context = {
    "form" : form
    }
    return render(request,"register.html",context)

def login(request):
    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(request,"Login Successfully")
            login_process(request, user)
            return redirect("index")

        messages.warning(request, "Username or password invalid")
        return render(request,"login.html",context)
    return render(request,"login.html",context)

@login_required
def logout(request):
    logout_process(request)
    messages.success(request,"Logout Successfully")
    return redirect("index")
