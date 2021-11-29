from rest_framework import generics
from rest_framework import response
from django.contrib.auth.models import auth , User
from rest_framework.views import APIView
from .serializers import   UserSerializer , ChangePasswordSerializer 
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User



class Login(APIView):
    def post(self, request, format=None):
        data = request.data

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

    def post(self, request, format=None):
        try:
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class ChangePasswordAPI(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self , username ):
        try:
            return User.objects.get(username = username)
        except User.DoesNotExist :
            return None
    
    def put(self , request):
        if request.user.username == request.data.get("username") :
            user = self.get_object(request.data.get("username"))
            if not user :
                return Response({'Not Found' : 'User does not exist'} , status = status.HTTP_400_BAD_REQUEST)
            user.set_password(request.data.get("new_password"))
            serializer = self.get_serializer(user , data = request.data , partial = True)
            if serializer.is_valid():
                user = serializer.save()
                return Response({"user": UserSerializer(user).data})
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Invalid Username" : "For changing password logged in username should be use."})