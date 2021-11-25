from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class BlogList(APIView):  # parent class is generics.ListCreateAPIView it allow to get all data and post the data

    # permission_classes = [IsAuthenticated]  # user must be logged in to get data
    # harishbhatt19@gmail.com
    def get(self, request):
        bolgs = Blog.objects.all()
        serializer = BlogSerializer(bolgs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetail(APIView):

    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise status.Http404
  
    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
