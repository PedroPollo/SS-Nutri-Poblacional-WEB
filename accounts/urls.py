from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name= "login"),
    path('logout/', views.logoutUser, name="logout"),
    path('indexadmin/', views.adminHome, name="IndexAdmin"),
    path('investigator/', views.investigatorHome, name="indexInvestigator"),
    path('adminUsers/', views.adminUsers, name="adminUsers"),
    path('adminSurveys/', views.adminSurvey, name="adminSurveys"),
    path('pollsters/', views.pollsters, name="pollsters"),
    path('invSurveys/', views.invSurveys, name="invSurvey")
] 