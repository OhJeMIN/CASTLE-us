from django.shortcuts import render, get_object_or_404, redirect
from .models import User_info, Company, Group_buying, Group_buying_comment, Flee_market, Review,Company_buying
from .forms import Group_buyingPost, Flee_marketPost
import random
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from datetime import date

from dateutil.relativedelta import *

def index(request):
    return render(request, 'index.html')
def loginPage(request):
    return render(request, 'login.html')
def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                request.session['user'] = user.id
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
    #로그인이 되어 있는지?
    user_pk = request.session.get('user')
    now = datetime.now()
    company = Company.objects.all()
    # now = now.strftime('%Y-%m-%d')
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        user_info = User_info.objects.all()
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment

        #메인_공동구매
        group_buying = Group_buying.objects.all()
        num=[]
        for i in group_buying:
            num+=[i.id]        
        randomNum = random.sample(num , 5)        
        randomObjList=[]
        for i in randomNum:
            randomObjList += Group_buying.objects.filter(id=i)
        #company_buying
        company_buying = Company_buying.objects.all()
        num=[]
        for i in company_buying:
            num+=[i.id]       
        randomNum1 = random.sample(num , 5)
        randomObjList1=[]
        for i in randomNum1:
            randomObjList1.append(list(Company_buying.objects.filter(id=i)))

        year = []
        for i in randomObjList1:
            year.append(i[0].finish_date.year)

        month = []
        for i in randomObjList1:
            month.append(i[0].finish_date.month)

        day = []
        for i in randomObjList1:
            day.append(i[0].finish_date.day)

        
        d_day = {}
        for i in range(len(year)):
            d_day[i]=int(relativedelta(datetime(year[i], month[i], day[i]), now).days)
        
            # d_day.insert(randomObjList[i].id, relativedelta(datetime(year[i], month[i], day[i]), now).days)
        for i in range(len(year)):
            print(randomObjList1[i])
            randomObjList1[i] += [d_day[i]]
            print()
        num = [0, 1]


        return render(request, 'main.html',  {'num': num, 'd_day': d_day,'company': company, 'date': date, 'user_info': user_info, 'group_buying': randomObjList,'company_buying':randomObjList1, 'apartment':apartment})
    #로그인이 되어있지 않으면?
    else:
        return redirect('/')

    

def group_board(request):
    #로그인이 되어 있는지?
    user_pk = request.session.get('user')
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
            isUser = False
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment
            isUser=True

        #메인_공동구매
        group_buying = Group_buying.objects.all()
        groupQuery = request.GET.get('groupSearch')
        if groupQuery:
            group_buying = Group_buying.objects.filter(title__contains = groupQuery)
            group_buying_list = Group_buying.objects.filter(title__contains =groupQuery).all()
            paginator = Paginator(group_buying, 10)
            page = request.GET.get('page')
            posts = paginator.get_page(page)    #페이지 번호 받아 해당 페이지 리턴
                    # [2]
            page_numbers_range = 10
            
            # [3]
            max_index = len(paginator.page_range)
            current_page = int(page) if page else 1
            start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
            end_index = start_index + page_numbers_range
            
            # [4]
            if end_index >= max_index:
                end_index = max_index
            paginator_range = paginator.page_range[start_index:end_index]
            return render(request, 'group_board.html', {'group_buying_search': group_buying, 'posts': posts, 'groupQuery': groupQuery, 'apartment':apartment, 'paginator_range':paginator_range, 'isUser':isUser})
        else:
            group_buying = Group_buying.objects
            group_buying_list = Group_buying.objects.all()
            group_buying_comment = Group_buying_comment.objects
            userinfo = User_info.objects
            paginator = Paginator(group_buying_list, 10)
            page = request.GET.get('page')
            posts = paginator.get_page(page)    #페이지 번호 받아 해당 페이지 리턴
                    # [2]
            page_numbers_range = 10
            
            # [3]
            max_index = len(paginator.page_range)
            current_page = int(page) if page else 1
            start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
            end_index = start_index + page_numbers_range
            
            # [4]
            if end_index >= max_index:
                end_index = max_index
            paginator_range = paginator.page_range[start_index:end_index]
           
            return render(request, 'group_board.html',{'group_buying':group_buying, 'group_buying_comment':group_buying_comment,'userinfo':userinfo, 'posts': posts, 'apartment':apartment,'paginator_range':paginator_range, 'isUser':isUser})

    else:
        return redirect('/')

    
def group_board_new(request, category):
    user_pk = request.session.get('user')
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment

        temp = Group_buying.objects.filter(category=category)
        group_buying_list = Group_buying.objects.filter(category = category).all()
        paginator = Paginator(temp, 10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)    #페이지 번호 받아 해당 페이지 리턴
                # [2]
        page_numbers_range = 10
        
        # [3]
        max_index = len(paginator.page_range)
        current_page = int(page) if page else 1
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        
        # [4]
        if end_index >= max_index:
            end_index = max_index
        paginator_range = paginator.page_range[start_index:end_index]
        return render(request, 'group_board.html', {'group_buying_filter':temp, 'posts': posts, 'paginator_range':paginator_range,'apartment':apartment})
    else:
        return redirect('/')

def company_detail (request, id):
    user_pk = request.session.get('user')
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
            isCompany = True
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment
            isCompany = False
        company_detail = get_object_or_404(Company_buying, pk=id)
        company = Company.objects
        userinfo = User_info.objects
        review = Review.objects
        return render(request, 'company_detail.html', {'company_detail':company_detail, 'company':company, 'userinfo':userinfo, 'review':review, 'isCompany':isCompany, "apartment":apartment})

    else:
        return redirect('/')

def register(request):
    return render(request, 'register1.html')

def register2(request):
    if request.method=='POST':
        user = User.objects.create_user(request.POST['username'],request.POST['username'] ,request.POST['password'])
        user.first_name = request.POST.get('firstname')
        temp = get_object_or_404(User, username=user.username)
        info = User_info()
        info.user_id = temp.id
        info.nickname = temp.username
        info.apartment = request.POST['apartment']
        info.address = request.POST['address']
        info.phone = request.POST['phone']
        if request.POST['firstname']=='사업자':
            info.isUser=False
            user.first_name='사업자'
        else:
            info.isUser=True
            user.first_name='개인'
       
        info.save()
        user.save()
        return redirect('/main')
    else :
        return render(request, 'register2.html')


def registerc(request):
    if request.method=='POST':
        user = User.objects.create_user(request.POST['username'],request.POST['username'] ,request.POST['password'])
        user.first_name = request.POST.get('firstname')
        cinfo = Company()
        cinfo.user_id=user.id
        cinfo.contents = request.POST['ctext']
        cinfo.img = request.POST['cimg']
        cinfo.phone = request.POST['phone']
        cinfo.name = request.POST['cname']
        if request.POST['firstname']=='사업자':
            user.first_name='사업자'
        else:
            user.first_name='개인'
       
        cinfo.save()
        user.save()
        return redirect('/main')
    else :
        return render(request, 'registerc.html')
    
    

def register3(request):
    return render(request, 'register3.html')

def Lcompany(request):
    return render(request, 'Lcompany.html')

def companyBuying(request):
    user_pk = request.session.get('user')
    now = datetime.now()
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
            isCompany = True
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment
            isCompany = False

        query2=request.GET.get('search123')
        if query2:
            companyBuying = Company_buying.objects.filter(title__contains=query2)
            companyinfo = Company.objects.all()
            paginator = Paginator(companyBuying, 20)
            page = request.GET.get('page')
            posts = paginator.get_page(page)    #페이지 번호 받아 해당 페이지 리턴
                    # [2]
            page_numbers_range = 10
            
            # [3]
            max_index = len(paginator.page_range)
            current_page = int(page) if page else 1
            start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
            end_index = start_index + page_numbers_range
            
            # [4]
            if end_index >= max_index:
                end_index = max_index
            paginator_range = paginator.page_range[start_index:end_index]


            year = []
            for i in posts:
                year.append(i.finish_date.year)

            month = []
            for i in posts:
                month.append(i.finish_date.month)

            day = []
            for i in posts:
                day.append(i.finish_date.day)

            d_day={}
            for i in range(len(year)):
                d_day[i]=int(relativedelta(datetime(year[i], month[i], day[i]), now).days)

            post=[]
            for i in posts:
                post.append([i])
            
            for i in range(len(year)):
                print(post[i])
                post[i] += [d_day[i]]
                print(post[i])
            
            return render(request, 'Company_buying.html',{'posts':posts,'apartment':apartment,'companyBuying':companyBuying, 'companyinfo':companyinfo, 'isCompany':isCompany, 'post': post, 'apartment':apartment,'paginator_range':paginator_range})
        else:
            companyBuying = Company_buying.objects.all()
            companyinfo = Company.objects.all()
            paginator = Paginator(companyBuying, 20)
            page = request.GET.get('page')
            posts = paginator.get_page(page)    #페이지 번호 받아 해당 페이지 리턴
                    # [2]
            page_numbers_range = 10
            
            # [3]
            max_index = len(paginator.page_range)
            current_page = int(page) if page else 1
            start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
            end_index = start_index + page_numbers_range
            
            # [4]
            if end_index >= max_index:
                end_index = max_index
            paginator_range = paginator.page_range[start_index:end_index]
           
           
            year = []
            for i in posts:
                year.append(i.finish_date.year)

            month = []
            for i in posts:
                month.append(i.finish_date.month)

            day = []
            for i in posts:
                day.append(i.finish_date.day)

            d_day={}
            for i in range(len(year)):
                d_day[i]=int(relativedelta(datetime(year[i], month[i], day[i]), now).days)

            post=[]
            for i in posts:
                post.append([i])
            
            for i in range(len(year)):
                print(post[i])
                post[i] += [d_day[i]]
                print(post[i])
                
            return render(request, 'Company_buying.html',{'apartment':apartment,'companyBuying':companyBuying, 'companyinfo':companyinfo, 'isCompany':isCompany,'post':post, 'posts': posts, 'apartment':apartment,'paginator_range':paginator_range})
        
    else:
        return redirect("/")



def fleaMarket(request):
    #로그인이 되어 있는지?
    user_pk = request.session.get('user')
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
            isUser = False
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment
            isUser=True

        query=request.GET.get('search')
        if query:
            fleaMarket = Flee_market.objects.filter(title__contains=query)
            paginator = Paginator(fleaMarket, 20)
            page = request.GET.get('page')
            posts = paginator.get_page(page)    #페이지 번호 받아 해당 페이지 리턴
                    # [2]
            page_numbers_range = 10
            
            # [3]
            max_index = len(paginator.page_range)
            current_page = int(page) if page else 1
            start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
            end_index = start_index + page_numbers_range
            
            # [4]
            if end_index >= max_index:
                end_index = max_index
            paginator_range = paginator.page_range[start_index:end_index]
            return render(request, 'fleaMarket.html', {'fleaMarket':fleaMarket, 'posts': posts, 'apartment':apartment, 'paginator_range':paginator_range, 'isUser':isUser})
        else:
            fleaMarket = Flee_market.objects.all()
            paginator = Paginator(fleaMarket, 20)
            page = request.GET.get('page')
            posts = paginator.get_page(page)    #페이지 번호 받아 해당 페이지 리턴
                    # [2]
            page_numbers_range = 10
            
            # [3]
            max_index = len(paginator.page_range)
            current_page = int(page) if page else 1
            start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
            end_index = start_index + page_numbers_range
            
            # [4]
            if end_index >= max_index:
                end_index = max_index
            paginator_range = paginator.page_range[start_index:end_index]
           
            return render(request, 'fleaMarket.html', {'fleaMarket':fleaMarket, 'posts': posts, 'apartment':apartment,'paginator_range':paginator_range, 'isUser':isUser})
    else:
        return redirect('/')

def fleaMarket_detail(request, id):
    user_pk = request.session.get('user')
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
            isCompany = True
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment
            isCompany = False

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


    return render(request, 'fleaMarket_detail.html', { 'randomObjList':randomObjList,'fleaMarket': fleaMarket, 'fleaMarketAll': fleaMarketAll, 'user_info': user_info, 'apartment': apartment,'isCompany':isCompany})


def fleaMaket_detail_new(request):
    user_pk = request.session.get('user')
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
            isCompany = True
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment
            isCompany = False

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
        fleaMarket.apartment = apartment
        fleaMarket.save()
    return redirect('/fleaMarket_detail/'+str(fleaMarket.id))


def groupPurchase_detail(request, id):
    user_pk = request.session.get('user')
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
            isCompany = True
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment
            isCompany = False

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
    return render(request, 'groupPurchase_detail.html', {'count': count,'groupPurchase': groupPurchase, 'allComments': allComments, 'user_info': user_info, 'apartment': apartment})

def groupPurchase_detail_new(request):
    user_pk = request.session.get('user')
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
            isCompany = True
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment
            isCompany = False

        proceeding = request.POST['proceeding']
        category = request.POST['category']
        groupPurchase = Group_buying()
        groupPurchase.title = request.POST['title']
        groupPurchase.img = request.FILES['myfile']
        groupPurchase.proceeding = int(proceeding)
        groupPurchase.contents = request.POST['contents']
        groupPurchase.writer = request.user.id #로그인 한 id
        groupPurchase.category = int(category)
        #아파트값 넣기
        groupPurchase.apartment = apartment
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
    user_pk = request.session.get('user')
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
            isCompany = True
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment
            isCompany = False

        form = Flee_marketPost()
        return render(request, 'fleaMarket_form.html', {'form': form, 'apartment': apartment})

def groupPurchase_form(request):
    user_pk = request.session.get('user')
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
            isCompany = True
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment
            isCompany = False

        form = Group_buyingPost()
        return render(request, 'groupPurchase_form.html', {'form': form, 'apartment':apartment,})

def createUser(request):
    user = User()
    user.user_name = request.POST['user_name']
    user.password = request.POST['password']
    user.email = reuqest.POST['email']
    user.save()
    return redirect()

def fleaMarket_new(request,category):
    user_pk = request.session.get('user')
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
            isUser= False
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment
            isUser = True

        temp=Flee_market.objects.filter(category=category)
        paginator = Paginator(temp, 20)
        page = request.GET.get('page')
        posts = paginator.get_page(page)    #페이지 번호 받아 해당 페이지 리턴
                # [2]
        page_numbers_range = 10
        
        # [3]
        max_index = len(paginator.page_range)
        current_page = int(page) if page else 1
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        
        # [4]
        if end_index >= max_index:
            end_index = max_index
        paginator_range = paginator.page_range[start_index:end_index]
            
        return render(request, 'fleaMarket.html', {'fleaMarket':temp, 'posts': posts, 'apartment':apartment,'paginator_range':paginator_range, 'isUser':isUser})
    else:
        return redirect('/')

def companyBuying_new(request,category):
    user_pk = request.session.get('user')
    now = datetime.now()
    if user_pk:
        user = get_object_or_404(User, id = user_pk)
        if user.first_name == '사업자':
            #사업자명
            apartment = get_object_or_404(Company, user_id = user_pk)
            apartment = apartment.name
            isUser= False
        else:
            #아파트
            apartment = get_object_or_404(User_info, user_id = user_pk)
            apartment = apartment.apartment
            isUser = True
        temp=Company_buying.objects.filter(category=category)
        companyinfo = Company.objects.all()
        paginator = Paginator(temp, 20)
        page = request.GET.get('page')
        posts = paginator.get_page(page)    #페이지 번호 받아 해당 페이지 리턴
                # [2]
        page_numbers_range = 10
        
        # [3]
        max_index = len(paginator.page_range)
        current_page = int(page) if page else 1
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        
        # [4]
        if end_index >= max_index:
            end_index = max_index
        paginator_range = paginator.page_range[start_index:end_index]
    
    
        year = []
        for i in posts:
            year.append(i.finish_date.year)

        month = []
        for i in posts:
            month.append(i.finish_date.month)

        day = []
        for i in posts:
            day.append(i.finish_date.day)

        d_day={}
        for i in range(len(year)):
            d_day[i]=int(relativedelta(datetime(year[i], month[i], day[i]), now).days)

        post=[]
        for i in posts:
            post.append([i])
        
        for i in range(len(year)):
            print(post[i])
            post[i] += [d_day[i]]
            print(post[i])
        
        return render(request, 'Company_buying.html',{'companyBuying':temp, 'companyinfo':companyinfo,'post':post,'posts': posts, 'apartment':apartment,'paginator_range':paginator_range, 'isUser':isUser})


    else:
        return redirect('/')


def company_buying_form(request):
    return render(request, 'company_buying_form.html')

def company_buying_form_new(request):
    companyBuying = Company_buying()
    companyBuying.company_id = user_pk    
    category = request.POST['category']
    proceeding = request.POST['proceeding']
    companyBuying.title = request.POST['title']
    companyBuying.main_img = request.FILES['myfile1']
    companyBuying.detail_img1 = request.FILES['myfile2']
    companyBuying.detail_img2 = request.FILES['myfile3']
    companyBuying.contents = request.POST['contents']
    companyBuying.proceeding = int(proceeding)
    companyBuying.category = int(category)
    companyBuying.finish_date = request.POST['date']
    companyBuying.writer = request.user.id
    companyBuying.apartment = request.POST['apartment']
    companyBuying.contract = 0
    companyBuying.save()
    return redirect('company_detail/'+str(companyBuying.id))