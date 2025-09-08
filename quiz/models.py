from django.db import models
from django.contrib.auth.models import AbstractUser

# Extend User model
class User(AbstractUser):
    # You can add extra fields later if needed
    pass


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizzes")

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()

    def __str__(self):
        return self.text[:50]  # show first 50 chars


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responses")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.text[:30]}"
