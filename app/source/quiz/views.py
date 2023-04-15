from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AnswerForm
# Create your views here.

#問題と解答のリスト
questions = []
answers = []
#問題数のカウント
number = 0

def home(request):
    """
    ホーム画面の表示
    """
    return render(request, 'home.html', {})


def match(request):
    """
    クイズ
    """
    #chatGPT APIの実装
    


    form = AnswerForm()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
           answer = form.cleaned_data['answer']
           
        


    else:
        return render(request, 'match.html', {})    

def show_answer(request):
    """
    正誤表示
    """
    return render(request, 'answer.html', {})

def correct(request):
    """
    正解画面
    """
    return render(request, 'match.html', {})

def incorrect(request):
    """
    不正解画面
    """
    return render(request, 'match.html', {})