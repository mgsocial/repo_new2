from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def helloworld(request):
    return HttpResponse('Hello World !')


def login(request):
    return HttpResponse('로그인 되었습니다')


def signout(request):
    return HttpResponse('잘가')
