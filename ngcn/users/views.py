from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import User
from django.contrib.auth.decorators import login_required
from .forms import (
    RegisterForm,UpdateRegisterForm
    )

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'a new account created for {username} sccessfully')
            return redirect('/')
    
    else:
        form = RegisterForm()
    
    context = {
        'form':form
    }
    return render(request,'users/register.html',context)

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

    