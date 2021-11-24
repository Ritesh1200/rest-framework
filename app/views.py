from types import prepare_class

from rest_framework import permissions
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics
from rest_framework.permissions import  IsAuthenticated


class BlogList(generics.ListCreateAPIView):  # parent class is generics.ListCreateAPIView it allow to get all data and post the data

    permission_classes = [IsAuthenticated]  # user must be logged in to get data

    queryset = Blog.objects.all()   # queryset is used for returning all objects of Blog
    serializer_class = BlogSerializer   # this class is used for serialization

    
