
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.BlogList.as_view() , name= "blog-list" ),  # BlogList class call 
    path('<int:pk>', views.BlogDetail.as_view() , name= "blog-detail" ),  # BlogDetail class call 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzODAwODIzMywiaWF0IjoxNjM3OTIxODMzLCJqdGkiOiJiNWRkNzhjZjU2N2Q0OTRhOWUxYTcyNjAyZjFhNWI5OCIsInVzZXJfaWQiOjF9.FaTT_vdDYreSeoVF7i5pSWcO9ORFJSGVpoUvtlxzF4k",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3OTIyMTMzLCJpYXQiOjE2Mzc5MjE4MzMsImp0aSI6ImY2NTdmM2VhNzVjOTRiZjdiMjUxZDEyYzI4MmFiZDYwIiwidXNlcl9pZCI6MX0.gHIJcH_3vlCRH1ZxSzZ2ISD2q-JJgie4BiSjfkMIfR8"
}