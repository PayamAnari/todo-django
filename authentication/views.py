from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from authentication.serializers import RegisterSerializers, GetUserSerializers, LoginSerializers
from django.contrib.auth import authenticate
from authentication.models import User
from django.core.exceptions import ObjectDoesNotExist




class RegisterAPIView(GenericAPIView):
     
     serializer_class = RegisterSerializers

     def post(self, request):
          serializer = self.serializer_class(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response({"message": 'User created successfully!', "data": serializer.data}, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersAPIView(GenericAPIView):
   
   serializer_class = GetUserSerializers

   def get(self, request):
          users = User.objects.all()
          serializer = self.serializer_class(users, many=True)
          return Response(serializer.data, status=status.HTTP_200_OK)

   def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class LoginAPIView(GenericAPIView):
    
    serializer_class = LoginSerializers
    
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username= email, password= password)

        if user:
          serializer = self.serializer_class(user)

          return Response({'message': 'User logged in successfully!', 'data': serializer.data}, status=status.HTTP_200_OK)

        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)