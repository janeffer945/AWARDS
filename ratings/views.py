from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateProfileForm, DisplayProjectForm, UpdateProfileForm

from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from .models import Profile,Project,Rating
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework.views import APIView
# from .permissions import  IsAdminOrReadOnly
from ratings import serializer

# Create your views here.
def index(request):
   
    workks = Project.objects.all().order_by('-id')
    return render(request, 'all-awards/index.html',{'workks':workks})
#Create profile for updating projects
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    projects = Project.objects.filter(user_id=current_user.id)
    
    return render(request,"profile.html",{'profile':profile,'projects':projects})
@login_required(login_url='/accounts/login/')
def upload_project(request):
    if request.method == 'POST':
        form=DisplayProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project =form.save(commit=False)
            project.save()
            return redirect('/')
    else:
        form=DisplayProjectForm()
    return render(request,"all-awards/upload_project.html",{'form':form})