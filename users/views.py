from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import User
from django.contrib.auth.decorators import login_required
from .forms import (
    RegisterForm,UpdateRegisterForm
    )

def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f'{username} new account created for  ')
            return redirect('/')

    else:
        form = RegisterForm()
    return render(request , 'users/register.html',{'form':form})

@login_required
def update_user(request):
    if request.method == 'POST':
        form = UpdateRegisterForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,f'updated successfully')
            return redirect('/')
    
    else:
        form = UpdateRegisterForm(instance=request.user)

    return render(request,'users/register.html',{'form':form})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user  = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'please make sure your username and password are correct')
            return redirect('users:login')
    else:
        return render(request,'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')    

