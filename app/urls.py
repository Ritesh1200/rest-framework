
from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogList.as_view() , name= "blog-list" ),  # BlogList class call 
    path('<int:pk>', views.BlogDetail.as_view() , name= "blog-detail" ),  # BlogDetail class call 
]
