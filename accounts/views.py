
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):
    def post(self, request):
        
        ser_user = UserRegistrationSerializer(data=request.POST)
        if ser_user.is_valid():
            User.objects.create_user(
                username=ser_user.validated_data["username"],
                email=ser_user.validated_data["email"],
                password=ser_user.validated_data["password"]
                
                )
        
            return Response(ser_user.data)
        return Response(ser_user.errors)