from django import forms
from .models import Group_buying, Flee_market

class Group_buyingPost(forms.ModelForm):
    class Meta:
        model = Group_buying
        fields = ['proceeding', 'title', 'img', 'contents']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'titlefield form-control'}),
            'img': forms.FileInput(attrs = {'class': 'imgfield'}),
            'proceeding': forms.NumberInput(attrs = {'class': 'proceedingfield form-control', 'placeholder': "진행(1)/ 종료(2)"}),
        }

        labels = {
            'title': "제목",
            'img': "사진",
            'proceeding': "진행상황"
        }

    

class Flee_marketPost(forms.ModelForm):
    class Meta:
        model = Flee_market
        fields = ['proceeding', 'price','title', 'img', 'img1', 'img2', 'contents']
        widgets = {
            'proceeding': forms.NumberInput(attrs = {'class': 'proceedingfield form-control', 'placeholder': "진행(1)/ 종료(2)"}),
            'title': forms.TextInput(attrs = {'class': 'titlefield form-control'}),
            'img': forms.FileInput(attrs = {'class': 'imgfield'}),
            'img1': forms.FileInput(attrs = {'class': 'img1field'}),
            'img2': forms.FileInput(attrs = {'class': 'img2field'}),
            'price': forms.NumberInput(attrs = {'class': 'pricefield form-control', 'placeholder': "가격(원)을 입력해주세요"}),
        }

        labels = {
            'title': "제목",
            'img': "사진",
            'img1': "",
            'img2': "",
            'proceeding': "진행상황",
            'price': "가격",
            "contents": "상세 설명"
        }
