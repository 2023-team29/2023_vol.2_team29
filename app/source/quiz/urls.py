from django.urls import path
from . import views


urlpatterns = [
    path('match/', views.match, name='match'),
    path('', views.home, name='home'),
    path('answer/', views.show_answer, name='show_answer'),
    path('correct/', views.correct, name='correct'),
    path('')
]