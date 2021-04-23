from django.shortcuts import render,redirect,get_object_or_404
from .models import Campagin
from .forms import CampaginForm
from django.contrib.auth.decorators import login_required

def home(request):
    campagins = Campagin.objects.all()[:4]
    return render(request,'campagin/index.html',{'lists':campagins})

@login_required
def createCampagin(request):
    form = CampaginForm()
    if request.method == 'POST':
        form = CampaginForm(request.POST,request.FILES )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.admin = request.user
            obj.save()
            return redirect('/')
    
    return render(request,'campagin/create.html',{'form':form})

@login_required
def updateCampagin(request,id):
    post = get_object_or_404(Campagin,id=id)
    form = CampaginForm(instance=post)
    if request.method == 'POST':
        form = CampaginForm(request.POST , request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'campagin/create.html',{'form':form})


def listCampagin(request):
    lists = Campagin.objects.all().order_by('-date')
    return render(request,'campagin/lists.html',{'lists':lists})

def detailCampagin(request,id):
    post = get_object_or_404(Campagin,id=id)
    return render(request,'campagin/detail.html',{'object':post})

@login_required
def deleteCampagin(request,id):
    obj = get_object_or_404(Campagin,id=id)
    if request.POST:
        obj.delete()
        return redirect('/')
        

        