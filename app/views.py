from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import response
from django.contrib.auth.models import auth , User
from rest_framework.views import APIView
from .serializers import   UserSerializer , ChangePasswordSerializer  , ChangepasswordSerializer
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator



class Login(APIView):
    def post(self, request, format=None):
        data = self.request.data

        username = data.get('username', None)
        password = data.get('password', None)
        print(username , password)
        user =  auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class Registration(APIView):

    def post(self , request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        auth.logout(request)
        return Response(status=status.HTTP_200_OK)



class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

# class ChangePasswordView(APIView):

#     permission_classes = [IsAuthenticated]

#     def put(self , request , pk):
#         user = User.objects.get(pk = pk)
#         if user is None:
#             return response(status=status.HTTP_400_BAD_REQUEST)
#         if user.username != request.user.username:
#             return response(status=status.HTTP_400_BAD_REQUEST)

#         user.set_password(request.data.get("new_password"))