from django.shortcuts import render, get_object_or_404, redirect
from .models import User_info, Company, Group_buying, Group_buying_comment, Flee_market, Review,Company_buying
from .forms import Group_buyingPost, Flee_marketPost
import random
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/main')
            else:
                return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/login')
    return render(request, 'login.html')

def main(request):
    group_buying = Group_buying.objects.all()    
    randomNum = []
    for i in range(1, len(group_buying)+1):
        randomNum.append(i)
    randomNum = random.sample(randomNum, 4)
    randomObjList = []
    for i in range(len(randomNum)):
        for j in range(group_buying.count()):
            if randomNum[i] == group_buying[j].id:
                randomObjList.append(group_buying[j])
    return render(request, 'main.html',  {'group_buying': randomObjList})

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
    if request.method=='POST':
        user = User.objects.create_user(request.POST['username'], request.POST['password'], request.POST['firstname'])
        temp = get_object_or_404(User, username=user.username)
        info = User_info()
        info.user_id = temp.id
        info.nickname = temp.username
        info.apartment = request.POST['apartment']
        info.address = request.POST['address']
        info.save()
    return render(request, 'register2.html')
    

def register3(request):
    return render(request, 'register3.html')

def Lcompany(request):
    return render(request, 'Lcompany.html')

def companyBuying(request):
    companyBuying = Company_buying.objects.all()
    companyinfo = Company.objects.all()
    return render(request, 'Company_buying.html', {'companyBuying': companyBuying, 'companyinfo': companyinfo})

def fleaMarket(request):
    fleaMarket = Flee_market.objects.all()
    return render(request, 'fleaMarket.html',{'fleaMarket':fleaMarket})

def fleaMarket_detail(request, id):
    fleaMarket = get_object_or_404(Flee_market, pk =id)
    user_info = User_info.objects.all()
    fleaMarketAll = Flee_market.objects.all()
    randomNum = []
    randomObjList = []
    for i in range(1, len(fleaMarketAll)+1):
        randomNum.append(i)

    if(len(randomNum) > 4):
        randomNum = random.sample(randomNum, 4)

    for i in range(len(randomNum)):
        for j in range(fleaMarketAll.count()):
            if randomNum[i] == fleaMarketAll[j].id:
                randomObjList.append(fleaMarketAll[j])
    return render(request, 'fleaMarket_detail.html', {'randomObjList':randomObjList,'fleaMarket': fleaMarket, 'fleaMarketAll': fleaMarketAll, 'user_info': user_info})


def fleaMaket_detail_new(request):
    fleaMarket = Flee_market()
    category = request.POST['category']
    proceeding = request.POST['proceeding']
    fleaMarket.title = request.POST['title']
    fleaMarket.img = request.FILES['myfile1']
    fleaMarket.img1 = request.FILES['myfile2']
    fleaMarket.img2 = request.FILES['myfile3']
    fleaMarket.contents = request.POST['contents']
    fleaMarket.proceeding = int(proceeding)
    fleaMarket.category = int(category)
    fleaMarket.price = request.POST['price']
    fleaMarket.writer = request.user.id
    fleaMarket.save()
    return redirect('/fleaMarket_detail/'+str(fleaMarket.id))


def groupPurchase_detail(request, id):
    groupPurchase = get_object_or_404(Group_buying,pk=id)
    user_info = User_info.objects.all()
    allComments = Group_buying_comment.objects.all()
    count  = 0
    if(len(allComments) == 0):
        count = 0
    else:
        for i in range(len(allComments)):
            if(allComments[i].Group_buying_id == id):
                count = count + 1
    return render(request, 'groupPurchase_detail.html', {'count': count,'groupPurchase': groupPurchase, 'allComments': allComments, 'user_info': user_info})

def groupPurchase_detail_new(request):
    proceeding = request.POST['proceeding']
    category = request.POST['category']
    groupPurchase = Group_buying()
    groupPurchase.title = request.POST['title']
    groupPurchase.img = request.FILES['myfile']
    groupPurchase.proceeding = int(proceeding)
    groupPurchase.contents = request.POST['contents']
    groupPurchase.writer = request.user.id #로그인 한 id
    groupPurchase.category = int(category)
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

def createUser(request):
    user = User()
    user.user_name = request.POST['user_name']
    user.password = request.POST['password']
    user.email = reuqest.POST['email']
    user.save()
    return redirect()