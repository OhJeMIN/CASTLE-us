from django.shortcuts import render, get_object_or_404, redirect
from .models import User_info, Company, Group_buying, Group_buying_comment, Flee_market, Review,Company_buying

def index(request):
    return render(request, 'index.html')

def group_board(request):
    group_buying = Group_buying.objects
    group_buying_comment = Group_buying_comment.objects
    return render(request, 'group_board.html',{'group_buying':group_buying, 'group_buying_comment':group_buying_comment})

def company_detail (request, id):
    company_detail = get_object_or_404(Company_buying, pk=id);
    company = Company.objects
    userinfo = User_info.objects
    return render(request, 'company_detail.html', {'company_detail':company_detail, 'company':company, 'userinfo':userinfo})
