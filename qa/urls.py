# qa/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 도서에 대한 질문 리스트
    path('<int:book_id>/', views.question_list, name='question_list'),

    # 질문 추가
    path('<int:book_id>/ask/', views.ask_question, name='ask_question'),

    # 답변 추가
    path('answer/<int:question_id>/', views.answer_question, name='answer_question'),

    path('answers/<int:question_id>/', views.answer_list, name='answer_list'),




]

