# qa/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:book_id>/', views.question_list, name='question_list'),
    path('<int:book_id>/ask/', views.ask_question, name='ask_question'),
    path('answer/<int:question_id>/', views.answer_question, name='answer_question'),
]
