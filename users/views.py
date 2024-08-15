from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse 
from django.views import View        


from .models import User
from .serializers import UserSerializer



class PingView(view):

    def get(self, request):
        return HttpResponse("App is active")


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            return Response({
                'message': 'Registration successful',
                'data': {
                    'accessToken': str(token.access_token),
                    'user': serializer.data
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    
    def post(self, request):
        from django.contrib.auth import authenticate
        from rest_framework_simplejwt.tokens import RefreshToken

        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = RefreshToken.for_user(user)
            serializer = UserSerializer(user)
            return Response({
                'message': 'Login successful',
                'data': {
                    'accessToken': str(token.access_token),
                    'user': serializer.data
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)



class UserDetailView(APIView):

    def get_user(self, userId):
        try:
            return User.objects.get(userId=userId)
        except User.DoesNotExist:
            raise NotFound(detail='User not found')
    
    def get(self, request, userId):
        user = self.get_user(userId)
        serializer = UserSerializer(user)
        return Response(serializer.data)



