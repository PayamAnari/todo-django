from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from authentication.serializers import RegisterSerializers, GetUsersSerializers, LoginSerializer, GetUserSerializers
from django.contrib.auth import authenticate, logout
from authentication.models import User
from django.core.exceptions import ObjectDoesNotExist



class AuthUserAPIView(GenericAPIView):
      
      permission_classes = [permissions.IsAuthenticated]
      
      def get(self, request):
          user = request.user
          serializer = RegisterSerializers(user)
          return Response({'user':serializer.data}, status=status.HTTP_200_OK)

class RegisterAPIView(GenericAPIView):
     
     serializer_class = RegisterSerializers

     def post(self, request):
          serializer = self.serializer_class(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response({"message": 'User created successfully!', "data": serializer.data}, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersAPIView(GenericAPIView):
   
   serializer_class = GetUsersSerializers

   def get(self, request):
          users = User.objects.all()
          serializer = self.serializer_class(users, many=True)
          return Response(serializer.data, status=status.HTTP_200_OK)

class UserAPIView(GenericAPIView):
   
    serializer_class = GetUserSerializers

    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class LoginAPIView(GenericAPIView):
   
    authentication_classes = []
    
    serializer_class = LoginSerializer
    
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username= email, password= password)

        if user:
          serializer = self.serializer_class(user)

          return Response({'message': 'User logged in successfully!', 'data': serializer.data})

        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)




class LogOutAPIView(GenericAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        logout(request)
        return Response({'message': 'User logged out successfully!'}, status=status.HTTP_200_OK)



class DeleteUserAPIView(GenericAPIView):

     permission_classes = [permissions.IsAuthenticated]

     def delete(self, request, pk):
         user = User.objects.get(id=pk)
         user.delete()
         return Response({'message': 'User deleted successfully!'}, status=status.HTTP_200_OK)