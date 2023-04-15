from django.urls import path
from . import views


urlpatterns = [
    path('match/', views.match, name='match'),
    path('', views.home, name='home'),
    path('correct/', views.correct, name='correct'),
    path('incorrect/', views.incorrect, name='incorrect')
]