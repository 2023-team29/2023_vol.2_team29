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

# CSRFトークンの検証を無効化
@csrf_exempt
def home(request):
    """
    ホーム画面の表示
    """
    # ChatGPT APIを使用して文章を生成
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"""あなたは、クイズ作成のプロです。
                ジャンルは問わず、クイズを10問返してください。ただし、以下のつの条件に従うこと。
                ①回答は"{"a":"1", "b":"2", "c": "3"}"のようなキーと値がともに文字列であるような要素を10個もつ辞書1つを文字列化したものを返すこと。
                ②辞書のキーを問題、値を解答とする
                ③解答は文章ではなく単語にすること""",
        max_tokens=60,
    )
    
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