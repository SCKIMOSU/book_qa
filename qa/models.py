# qa/models.py
from django.db import models
from books.models import Book

class Question(models.Model):
    book = models.ForeignKey(Book, related_name="questions", on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question about {self.book.title} by {self.user_name}"

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer by {self.user_name} for {self.question}"
