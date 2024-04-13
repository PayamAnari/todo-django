from rest_framework import serializers
from authentication.models import User


class RegisterSerializers(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=6, write_only=True)


    class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email', 'password']

    
    def create(self, validated_data):
      return User.objects.create_user(**validated_data)

class GetUserSerializers(serializers.ModelSerializer):
  
      class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email', 'created_at', 'email_verified']