from django.shortcuts import render
from rest_framework.decorators import APIView
from .serializers import UserRegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class UserRegister(APIView):
    
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewset(viewsets.ViewSet):
    
    queryset = User.objects.all()
    
    def list(self, request):
        ser_data = UserSerializer(instance=self.queryset, many=True)
        return Response(ser_data.data)
    
    def retrieve(self, request, pk):
        user = get_object_or_404(self.queryset, pk=pk)
        if request.user != user:
            Response({"message":"not valid"})
        
        ser_data = UserSerializer(instance=user)
        return Response(ser_data.data)
    
    def partial_update(self, request, pk):
        user = get_object_or_404(self.queryset, pk=pk)
        
        if request.user != user:
            Response({"message":"permission denied: you are not the owner!"})
        
        ser_data = UserSerializer(instance=self.queryset, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
            
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        user = get_object_or_404(self.queryset, pk=pk)
        if request.user != user:
            Response({"message":"permission denied: you are not the owner!"})
        user.is_active = False
        user.save()
        return Response({"message": "user deactivated successfully!"}) 
