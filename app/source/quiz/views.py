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
counter = 0
points = 0

# CSRFトークンの検証を無効化
@csrf_exempt
def home(request):
    """
    ホーム画面の表示
    """
    counter = 0
    points = 0
    questions = []
    answers = []

    # ChatGPT APIを使用して文章を生成
    question = {"日本で一番高い山は？":"富士山"}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"""あなたは、クイズ作成のプロです。
                ジャンルは問わず、クイズを10問返してください。ただし、以下のつの条件に従うこと。
                ①回答は{question}のようなキーと値がともに文字列であるような要素をもつ辞書10個のリストを返すこと。
                ②辞書のキーを問題、値を解答とする
                ③解答は文章ではなく単語にすること""",
    )

    #問題と解答のリストへの格納
    response_list = list(response.to_dict()['completion'])
    for dic in response_list:
        for k, v in dic.items():
            questions.append(k)
            answers.append(v)
    
    return render(request, 'home.html', {})


def match(request):
    """
    クイズ
    """
    form = AnswerForm()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            correct_ans = answers[counter-1]


        if answer == correct_ans:
            #正解
            points += 1
            redirect('correct')
        else:
            #不正解
            redirect('incorrect')
        
    else:
        if counter >= 10:
            render(request, 'result.html', {'point': points})
        else:
            counter += 1
            render(request, 'match.html', {'form': form})
 


def correct(request):
    """
    正解画面
    """
    return render(request, 'correct.html', {})

def incorrect(request):
    """
    不正解画面
    """
    correct_ans = answers[counter-1]
    return render(request, 'incorrect.html', {'answer': correct_ans})