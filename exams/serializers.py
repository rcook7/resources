from django.contrib.auth.models import User
from rest_framework import serializers
from exams.models import Category, Test, Question

class CategorySerializer(serializers.ModelSerializer):
    tests = serializers.PrimaryKeyRelatedField(many=True, queryset=Test.objects.all())

    class Meta:
        model = Category
        fields = ('id', 'name', 'tests')


class TestSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())

    class Meta:
        model = Test
        fields = ('id', 'title', 'description', 'category', 'questions')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'type', 'question', 'answers', 'score', 'test')
