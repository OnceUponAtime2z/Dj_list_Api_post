from django.shortcuts import render
from django.http import HttpResponse


def Posts(request):
    return HttpResponse('List Post')

def index(request):
    id = ''
    user_Id = ''
    title = ''
    body = ''
    return render(request, 'index.html',{
        'id': id,
        'user_Id': user_Id,
        'title': title,
        'body': body,
    })