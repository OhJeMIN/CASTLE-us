"""hakertone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import app.views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app.views.index, name='index'),
    path('login', app.views.login, name='login'),
    path('logout', app.views.logout, name='logout'),
    path('main',app.views.main, name='main'),
    path('group_board',app.views.group_board, name='group_board'),
    path('company_detail/<int:id>', app.views.company_detail, name='company_detail'),
    path('register',app.views.register, name='register'),
    path('register2',app.views.register2, name='register2'),    
    path('register3',app.views.register3, name='register3'),    
    path('Lcompany',app.views.Lcompany, name='Lcompany'),
    
    path('companyBuying',app.views.companyBuying, name='companyBuying'),   
    path('fleaMarket',app.views.fleaMarket, name='fleaMarket'),   

    path('fleaMarket_detail/<int:id>', app.views.fleaMarket_detail, name='fleaMarket_detail'),
    path('groupPurchase_detail/<int:id>', app.views.groupPurchase_detail, name='groupPurchase_detail'),

    path('fleaMarket_form', app.views.fleaMarket_form, name='fleaMarket_form'),
    path('groupPurchase_form', app.views.groupPurchase_form, name = 'groupPurchase_form'),

    path('fleaMarket_detail_new', app.views.fleaMaket_detail_new, name='fleaMarket_detail_new'),
    path('groupPurchase_detail_new', app.views.groupPurchase_detail_new, name = 'groupPurchase_detail_new'),
    
    path('groupPurchase_comment_new', app.views.groupPurchase_comment_new, name= 'groupPurchase_comment_new'), 

    path('ckeditor/', include('ckeditor_uploader.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)