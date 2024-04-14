from rest_framework import serializers
from authentication.models import User


class RegisterSerializers(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=6, write_only=True)


    class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email', 'password']

    
    def create(self, validated_data):
      return User.objects.create_user(**validated_data)

class GetUsersSerializers(serializers.ModelSerializer):
  
      class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email', 'created_at', 'email_verified', 'is_superuser', 'is_active']


class GetUserSerializers(serializers.ModelSerializer):
    
        class Meta:
          model = User
          fields = ['id','username', 'first_name', 'last_name', 'email', 'created_at', 'email_verified', 'is_superuser', 'is_active']

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    class Meta:
      model = User
      fields = ['email', 'username', 'password', 'token']

      read_only_fields = ['token']


class UpdateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.save()
        return instance