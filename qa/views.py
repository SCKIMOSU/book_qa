# qa/views.py

from .forms import QuestionForm, AnswerForm
from books.models import Book
from .models import Question,Answer
from django.shortcuts import render, get_object_or_404, redirect



def question_list(request, book_id):
    # book_id로 책 객체를 가져옵니다.
    book = get_object_or_404(Book, id=book_id)

    # 해당 책에 대한 모든 질문을 가져옵니다.
    questions = book.questions.all()

    return render(request, 'qa/question_list.html', {
        'book': book,
        'questions': questions,
    })

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
    # 특정 질문을 가져옵니다.
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('answer_list', question_id=question.id)
    else:
        form = AnswerForm()

    return render(request, 'qa/answer_question.html', {'form': form, 'question': question})

def answer_list(request, question_id):
    # question_id로 특정 질문을 가져옵니다.
    question = get_object_or_404(Question, id=question_id)

    # 해당 질문에 대한 모든 답변을 가져옵니다.
    answers = question.answers.all()

    return render(request, 'qa/answer_list.html', {
        'question': question,
        'answers': answers,
    })
