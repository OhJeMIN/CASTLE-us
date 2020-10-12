from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def group_board(request):
    return render(request, 'group_board.html')
