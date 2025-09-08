from django.urls import path
from .views import (
    QuizListCreateView, QuizDetailView,
    QuestionListCreateView, OptionListCreateView,
    ResponseListCreateView, UserRegisterView
)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("quizzes/", QuizListCreateView.as_view(), name="quiz-list"),
    path("quizzes/<int:pk>/", QuizDetailView.as_view(), name="quiz-detail"),
    path("questions/", QuestionListCreateView.as_view(), name="question-list"),
    path("options/", OptionListCreateView.as_view(), name="option-list"),
    path("responses/", ResponseListCreateView.as_view(), name="response-list"),
]
