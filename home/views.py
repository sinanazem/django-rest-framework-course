from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer


class PersonView(APIView):
    def get(self, request):
        person = Person.objects.all()
        ser_person = PersonSerializer(instance=person, many=True)
        
        return Response(data = ser_person.data)