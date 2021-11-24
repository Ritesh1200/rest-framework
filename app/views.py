from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class BlogList(APIView):  # parent class is generics.ListCreateAPIView it allow to get all data and post the data

    permission_classes = [IsAuthenticated]  # user must be logged in to get data

    def get(self, request):
        snippets = Blog.objects.all()
        serializer = BlogSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
