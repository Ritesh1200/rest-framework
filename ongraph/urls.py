
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),  # this is for my admin panel
    path('api-auth/', include('rest_framework.urls')),  # this helps in login and logout
    path('', include( 'app.urls')),      # this call my app urls
]
# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzODAwNjIyMSwiaWF0IjoxNjM3OTE5ODIxLCJqdGkiOiI2ODU5OGNhZDNkYjg0N2ZmYWMwYzJmYWFkZGI2NDkxZiIsInVzZXJfaWQiOjF9.0WIchMM-K43pD5TKtZHyKcr21zJtLb5Chmwbnf0ke2s",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3OTIwMTIxLCJpYXQiOjE2Mzc5MTk4MjEsImp0aSI6ImU0NTk2MjQ2ZGFiMjQ3NTg4MTkyZDhiYmU2MWM0OGYyIiwidXNlcl9pZCI6MX0.HMTWjtggHCfmw8mXT-a5hzRdMwNuNB7MO4u8oIQJ3ak"
# }