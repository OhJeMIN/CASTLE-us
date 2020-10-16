from django.shortcuts import render, get_object_or_404, redirect
from .models import User_info, Company, Group_buying, Group_buying_comment, Flee_market, Review,Company_buying
from .forms import Group_buyingPost, Flee_marketPost
import random

def index(request):
    return render(request, 'index.html')

def group_board(request):
    group_buying = Group_buying.objects
    group_buying_comment = Group_buying_comment.objects
    userinfo = User_info.objects
    return render(request, 'group_board.html',{'group_buying':group_buying, 'group_buying_comment':group_buying_comment,'userinfo':userinfo})

def company_detail (request, id):
    company_detail = get_object_or_404(Company_buying, pk=id)
    company = Company.objects
    userinfo = User_info.objects
    review = Review.objects
    return render(request, 'company_detail.html', {'company_detail':company_detail, 'company':company, 'userinfo':userinfo, 'review':review})

def register(request):
    return render(request, 'register1.html')

def register2(request):
    return render(request, 'register2.html')

def register3(request):
    return render(request, 'register3.html')

def Lcompany(request):
    return render(request, 'Lcompany.html')

def companyBuying(request):
    companyBuying = Company_buying.objects.all()
    return render(request, 'Company_buying.html', {'companyBuying': companyBuying})

def fleaMarket(request):
    fleaMarket = Flee_market.objects.all()
    return render(request, 'fleaMarket.html',{'fleaMarket':fleaMarket})


def fleaMarket_detail(request, id):
    fleaMarket = get_object_or_404(Flee_market, pk =id)
    fleaMarketAll = Flee_market.objects.all()
    user_info = User_info.objects.all()
    fleaMarketAllList = []
    for i in fleaMarketAll:
        fleaMarketAllList.append(i.id)
    randomNum = random.sample(fleaMarketAllList, 4)
    return render(request, 'fleaMarket_detail.html', {'n':randomNum,'fleaMarket': fleaMarket, 'fleaMarketAll': fleaMarketAll, 'user_info': user_info})

def fleaMaket_detail_new(request):
    fleaMarket = Flee_market()
    fleaMarket.title = request.POST['title']
    fleaMarket.img = request.FILES['myfile1']
    fleaMarket.img1 = request.FILES['myfile2']
    fleaMarket.img2 = request.FILES['myfile3']
    fleaMarket.contents = request.POST['contents']
    fleaMarket.proceeding = request.POST['proceeding']
    fleaMarket.price = request.POST['price']
    fleaMarket.writer = request.user.id
    fleaMarket.save()
    return redirect('/fleaMarket_detail/'+str(fleaMarket.id))


def groupPurchase_detail(request, id):
    groupPurchase = get_object_or_404(Group_buying,pk=id)
    user_info = User_info.objects.all()
    allComments = Group_buying_comment.objects.all()
    return render(request, 'groupPurchase_detail.html', {'groupPurchase': groupPurchase, 'allComments': allComments, 'user_info': user_info})

def groupPurchase_detail_new(request):
    groupPurchase = Group_buying()
    groupPurchase.title = request.POST['title']
    groupPurchase.img = request.FILES['myfile']
    groupPurchase.proceeding = request.POST['proceeding']
    groupPurchase.contents = request.POST['contents']
    groupPurchase.writer = request.user.id #로그인 한 id
    groupPurchase.save()
    return redirect('/groupPurchase_detail/'+ str(groupPurchase.id))

def groupPurchase_comment_new(request):
    groupPurchaseComment = Group_buying_comment()
    groupPurchaseComment.Group_buying_id = request.GET['groupPurchase_id'] #어떤 글의 댓글인지 group_buying id 값
    groupPurchaseComment.user_info_id = request.user.id #누가 쓴 댓글인지 user_info id값
    groupPurchaseComment.contents = request.GET['contents']
    groupPurchaseComment.save()
    return redirect('/groupPurchase_detail/'+ str(groupPurchaseComment.Group_buying_id))

def fleaMarket_form(request):
    form = Flee_marketPost()
    return render(request, 'fleaMarket_form.html', {'form': form})

def groupPurchase_form(request):
    form = Group_buyingPost()
    return render(request, 'groupPurchase_form.html', {'form': form})

