from rest_framework import serializers

def clean_email(value):
    if "admin" in value :
        raise serializers.ValidationError("email not valid!")
    return value


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[clean_email])
    password = serializers.CharField(required=True, write_only=True)
    password_c = serializers.CharField(required=True, write_only=True)
    
    def validate_username(self, value):
        if value == "admin":
            raise serializers.ValidationError("your username not valid!")
        return value
    
    def validate(self, data):
        if data["password"] != data["password_c"]:
            raise serializers.ValidationError("passwords not match!")
        
        return data


