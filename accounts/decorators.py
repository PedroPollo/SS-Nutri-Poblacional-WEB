from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwars):
        if request.user.is_authenticated:
            return redirect('IndexAdmin')
        else:
            return view_func(request, *args, **kwars)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwars):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwars)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwars):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Investigador':
            return redirect('indexInvestigator')
        
        if group == 'Administrador':
            return view_func(request, *args, **kwars)
        
    
    return wrapper_func

def investigator_only(view_func):
    def wrapper_func(request, *args, **kwars):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Administrador':
            return redirect('IndexAdmin')
        
        if group == 'Investigador':
            return view_func(request, *args, **kwars)
        
    
    return wrapper_func