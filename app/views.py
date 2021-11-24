from types import prepare_class

from rest_framework import permissions
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics
from rest_framework.permissions import  IsAuthenticated


class BlogList(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    
