from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .models import Person
from .serializers import PersonSerializer


class HomeView(APIView):
    def get(self, request):
        person = Person.objects.all()
        ser_data = PersonSerializer(instance=person, many=True)
        
        return Response(ser_data.data)

# @api_view(['GET', 'POST'])
# def home(request):
#     return Response({'name': 'ali',})


# class HomeView(View):
#     def get(self, request):
#         return render(request, 'home/home.html')
