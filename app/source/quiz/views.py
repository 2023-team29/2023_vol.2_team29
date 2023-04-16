from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AnswerForm
import os
import openai
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Create your views here.

# APIキーを設定
openai.api_key = settings.API_KEY

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

           if a == b:
               #正解
               redirect('correct')
           else:
               #不正解
               redirect('incorrect')
           
        else:
            render(request, 'match.html', {'form': form})
        


    else:
        return render(request, 'match.html', {'form': form})    


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