from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from .models import Quiz, Question, Option, Response as QuizResponse
from .serializers import (
    QuizSerializer,
    QuestionSerializer,
    OptionSerializer,
    ResponseSerializer,
    UserSerializer,
)

def api_root(request, format=None):
    return Response({
        'register': reverse('register', request=request, format=format),
        'quizzes': reverse('quiz-list-create', request=request, format=format),
        'response': reverse('response-list-create', request=request, format=format),
    })
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

