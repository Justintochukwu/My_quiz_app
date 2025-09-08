from rest_framework import serializers
from .models import User, Quiz, Question, Option, Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ["id", "text", "is_correct"]


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "text", "options"]


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ["id", "title", "description", "created_at", "questions"]


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ["id", "user", "question", "option", "answered_at"]
