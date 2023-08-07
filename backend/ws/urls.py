from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_view, name='chat'),
    path('', views.index.as_view(), name='index'),
    path('get-users/',views.get_user.as_view()),
]
