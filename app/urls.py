
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login.as_view() , name= "login" ),  
    path('registration', views.Registration.as_view() , name= "registration" ),   
    path('logout', views.LogoutView.as_view(), name='auth_logout'),
    path('changepassword/', views.ChangePasswordAPI.as_view(), name='changepassword'),



]
