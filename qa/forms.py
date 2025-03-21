# qa/forms.py
from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['user_name', 'content']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['user_name', 'content']
