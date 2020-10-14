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


def groupParchase_detail(request, id):
    groupParchase = get_object_or_404(Group_buying,pk=id)
    allComments = Group_buying_comment.objects
    return render(request, 'groupParchase_detail.html', {'groupParchase': groupParchase, 'allComments': allComments})

def groupParchase_detail_new(request):
    groupParchase = Group_buying()
    groupParchase.title = request.POST['title']
    groupParchase.img = request.POST.get('img')
    groupParchase.proceeding = request.POST['proceeding']
    groupParchase.contents = request.POST['contents']
    groupParchase.writer = request.user.id #로그인 한 id
    groupParchase.save()
    return redirect('/groupParchase_detail/'+ str(groupParchase.id))

def groupParchase_comment_new(request):
    groupParchaseComment = Group_buying_comment()
    groupParchaseComment.Group_buying_id = request.GET['groupParchase_id'] #어떤 글의 댓글인지 group_buying id 값
    groupParchaseComment.user_info_id = request.user.id #누가 쓴 댓글인지 user_info id값
    groupParchaseComment.contents = request.GET['contents']
    groupParchaseComment.save()
    return redirect('/groupParchase_detail/'+ str(groupParchaseComment.Group_buying_id))

def fleaMarket_form(request):
    return render(request, 'fleaMarket_form.html')

def groupParchase_form(request):
    form = Group_buyingPost()
    return render(request, 'groupParchase_form.html', {'form': form})

