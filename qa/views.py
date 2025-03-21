# qa/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from books.models import Book
from .forms import QuestionForm, AnswerForm


def question_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    questions = book.questions.all()
    return render(request, 'qa/question_list.html', {'book': book, 'questions': questions})


def ask_question(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.book = book
            question.save()
            return redirect('question_list', book_id=book.id)
    else:
        form = QuestionForm()

    return render(request, 'qa/ask_question.html', {'form': form, 'book': book})


def answer_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('question_list', book_id=question.book.id)
    else:
        form = AnswerForm()

    return render(request, 'qa/answer_question.html', {'form': form, 'question': question})
