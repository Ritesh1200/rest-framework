
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login.as_view() , name= "login" ),  
    path('registration', views.Registration.as_view() , name= "registration" ),   
    path('logout', views.LogoutView.as_view(), name='auth_logout'),
    path('change_password/<int:pk>', views.ChangePasswordView.as_view(), name='auth_change_password'),


]
