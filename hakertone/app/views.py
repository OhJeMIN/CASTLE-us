from django.shortcuts import render, get_object_or_404, redirect
from .models import User_info, Company, Group_buying, Group_buying_comment, Flee_market, Review,Company_buying

def index(request):
    return render(request, 'index.html')

def group_board(request):
    group_buying = Group_buying.objects
    group_buying_comment = Group_buying_comment.objects
    return render(request, 'group_board.html',{'group_buying':group_buying, 'group_buying_comment':group_buying_comment})

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

def Ccompany(request):
    return render(request, 'Ccompany.html')

def Pcompany(request):
    return render(request, 'Pcompany.html')


def fleaMarket_detail(request, id):
    fleaMarket = get_object_or_404(Flee_market, pk =id)
    return render(request, 'fleaMarket_detail.html', {'fleaMarket': fleaMarket})

def fleaMaket_detail_new(request):
    fleaMarket = Flee_market()
    fleaMarket.title = request.GET['title']
    fleaMarket.img = request.GET['img']
    fleaMarket.contents = request.GET['contents']
    fleaMarket.proceeding = request.GET['proceeding']
    fleaMarket.price = request.GET['price']
    fleaMarket.writer = User.objects.get(username= request.user.get_username())
    fleaMarket.save()
    return redirect('/fleaMarket_detail/'+str(fleaMarket.id))


def groupPurchase_detail(request, id):
    groupPurchase = get_object_or_404(Group_buying,pk=id)
    allComments = Group_buying_comment.objects
    return render(request, 'groupPurchase_detail.html', {'groupPurchase': groupPurchase, 'allComments': allComments})

def groupPurchase_detail_new(request):
    groupPurchase = Group_buying()
    groupPurchase.title = request.POST['title']
    groupPurchase.img = request.POST.get('img')
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
    return render(request, 'fleaMarket_form.html')

def groupPurchase_form(request):
    form = Group_buyingPost()
    return render(request, 'groupPurchase_form.html', {'form': form})

