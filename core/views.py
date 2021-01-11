from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from .forms import QuestionForm, AnswerForm
# Create your views here.


def list_questions(request):
    question = Question.objects.all()

    return render(request, 'html/index.html', {'question': question})

def edit_questions(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'GET':
        form = QuestionForm(instance=question)
    else: 
        form = QuestionForm(data=request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect(to='list-questions')
    return render(request, "html/edit_question.html", {
        'form': form,
        "question": question
    })

def add_answer(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'GET':
        form = AnswerForm()
    else: 
        form = AnswerForm(data=request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect(to='list-questions')
    return render(request, "html/answer_question.html", {
        'form': form,
        "question": question
    })