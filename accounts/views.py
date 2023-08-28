from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import Group

from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only, investigator_only
from .models import *


# Create your views here.
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='Investigador')
            group.user_set.add(user)

            messages.success(request,'Cuenta creada para '+ form.cleaned_data.get('nombre'))

            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('IndexAdmin')
        else:
            messages.info(request,'Username or Password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
@admin_only
def adminHome(request):
    context = {}
    return render(request, 'accounts/index.html',context)

@login_required(login_url='login')
@admin_only
def adminUsers(request):
    users = User.objects.filter(is_superuser = False)
    return render(request, 'accounts/admin/users.html', {'users':users})

@login_required(login_url='login')
@admin_only
def adminSurvey(request):
    context = {}
    return render(request, 'accounts/admin/surveys.html', context)

@login_required(login_url='login')
@investigator_only
def investigatorHome(request):
    context = {}
    return render(request, 'accounts/index.html', context)

@login_required(login_url='login')
@investigator_only
def pollsters(request):
    context = {}
    return render(request, 'accounts/investigator/encuestadores.html', context)

@login_required(login_url='login')
@investigator_only
def invSurveys(request):
    context = {}
    return render(request, 'accounts/investigator/surveys.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def deleteUser(request,id):
    user = User.objects.get(id=id)
    User.delete(user)

    return redirect('../')