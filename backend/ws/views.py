from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes


def chat_view(request):
    return render(request, 'chat.html')

@authentication_classes([])
class index(APIView):
    def get(self,request):
        return render(request, 'index.html')


@authentication_classes([])
class get_user(APIView):
    def post(self,request):
        print(request.user)
        return Response({})