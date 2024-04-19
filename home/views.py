from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .models import Person, Question, Answer
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

class HomeView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        person = Person.objects.all()
        ser_data = PersonSerializer(instance=person, many=True)
        
        return Response(ser_data.data)


class QuestionView(APIView):
    permission_classes = [AllowAny, ]
    
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)
        
    
    def post(self, request):
        ser_data = QuestionSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        ser_data = QuestionSerializer(instance=question ,data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({"message":"you question deleted successfully!"}, status=status.HTTP_200_OK)

# @api_view(['GET', 'POST'])
# def home(request):
#     return Response({'name': 'ali',})


# class HomeView(View):
#     def get(self, request):
#         return render(request, 'home/home.html')
