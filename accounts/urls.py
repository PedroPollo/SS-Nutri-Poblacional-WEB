from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('indexadmin/', views.adminHome, name="IndexAdmin"),
    path('investigator/', views.investigatorHome, name="indexInvestigator"),
    path('adminUsers/', views.adminUsers, name="adminUsers"),
    path('adminSurveys/', views.adminSurvey, name="adminSurveys"),
    path('pollsters/', views.pollsters, name="pollsters"),
    path('invSurveys/', views.invSurveys, name="invSurvey"),
    path('adminUsers/deleteUser/<id>', views.deleteUser, name="deleteUser"),
    path('dashboard/', views.index, name="index"),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-reset/', views.password_reset.as_view(), name='password_reset'),
    path('analisis/', views.analisis, name='analisis'),
    path('billing/', views.billing, name='billing'),
    path('vr/', views.vr, name='vr'),
    path('rtl/', views.rtl, name='rtl'),
    path('profile/', views.profile, name='profile')

]
