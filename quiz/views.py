from rest_framework import generics
from django.contrib.auth import get_user_model
from .models import Quiz, Question, Option, Response
from .serializers import (
    QuizSerializer,
    QuestionSerializer,
    OptionSerializer,
    ResponseSerializer,
    UserSerializer,
)

# List all quizzes / create new quiz
class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


# Retrieve, update, delete a quiz
class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


# Questions
class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# Options
class OptionListCreateView(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


# Responses
class ResponseListCreateView(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


# User Registration
User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

