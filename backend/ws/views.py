from django.shortcuts import render

def chat_view(request):
    return render(request, 'chat.html')

def index(request):
    return render(request, 'index.html')