from django.urls import path
from . import views


urlpatterns = [
    path('match/', views.match, name='match'),
    path('', views.home, name='home'),
    path('', views.show_answer, name='show_answer'),
]