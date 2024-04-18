from django.shortcuts import render
from rest_framework.decorators import APIView
from .serializers import UserRegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response

class UserRegister(APIView):
    
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data)
        
        return Response(ser_data.errors)
            
