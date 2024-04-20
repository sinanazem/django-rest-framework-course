from rest_framework import serializers
from django.contrib.auth.models import User


def clean_email(value):
    if 'admin' in value.lower():
        raise serializers.ValidationError("email can not include `admin` ")
    return value


class UserRegisterSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(required=True, write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        
        extra_kwargs = {
            
            'email':{
                'validators': [clean_email, ],
            },
            
            'password':{
                'write_only': True,
                
            },
        }
    
    def create(self, validated_data):
        del validated_data['confirm_password']
        return User.objects.create_user(**validated_data)
    
    def validate_username(self, value):
        
        if value.lower() == 'admin':
            raise serializers.ValidationError('username can not be `admin` ')
        return value
    
    def validate(self, data):
        
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('passwords are not match!')
        return data



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"