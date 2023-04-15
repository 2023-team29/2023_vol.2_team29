from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AnswerForm
# Create your views here.

def home(request):
    """
    ホーム画面の表示
    """
    return render(request, 'quiz/home.html', {})


def match(request):
    """
    クイズ
    """
    form = AnswerForm()
    if request.method == 'POST':


    else:
        return render(request, 'quiz/match.html', {})    

def show_answer(request):
    """
    正誤表示
    """

