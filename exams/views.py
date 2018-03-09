from django.shortcuts import render
from rest_framework import viewsets, status, renderers
from rest_framework.decorators import api_view, detail_route
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .models import Test, Question, Category
from .serializers import TestSerializer, QuestionSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @detail_route()
    def getTests(self, request, *args, **kwargs):
        """
        Get tests of a category
        """
        testQuery = Test.objects.filter(category=kwargs['pk'])
        serializer = TestSerializer(testQuery, many=True)
        return Response(serializer.data)

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    @detail_route()
    def getQuestions(self, request, *args, **kwargs):
        """
        Get questions of a test
        """
        questionQuery = Question.objects.filter(test=kwargs['pk'])
        serializer = QuestionSerializer(questionQuery, many=True)
        return Response(serializer.data)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

@api_view(['GET'])
def exams_root(request, format=None):
    return Response({
        'categories': reverse('category-list', request=request, format=format),
        'tests': reverse('test-list', request=request, format=format),
        'questions': reverse('question-list', request=request, format=format),
    })