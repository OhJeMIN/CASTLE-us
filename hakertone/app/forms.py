from django import forms
from .models import Group_buying, Flee_market


class Group_buyingPost(forms.ModelForm):
    class Meta:
        model = Group_buying
        fields = ['title', 'contents']
        # fields = ['proceeding','category', 'title', 'contents']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'titlefield form-control'}),
            # 'proceeding': forms.NumberInput(attrs = {'class': 'proceedingfield form-control', 'placeholder': "진행(1)/ 종료(2)"}),
            # 'category': forms.NumberInput(attrs={'class': 'categoryfield form-control'}),
        }
        labels = {
            'title': "제목",
            'contents': "내용",
            # 'proceeding': "진행상황",
            # 'category': "카테고리"
        }

    

class Flee_marketPost(forms.ModelForm):
    class Meta:
        model = Flee_market
        fields = ['price','title', 'contents']
        # fields = ['proceeding', 'category', 'price','title', 'contents']
        widgets = {
            # 'proceeding': forms.NumberInput(attrs = {'class': 'proceedingfield form-control', 'placeholder': "진행(1)/ 종료(2)"}),
            'title': forms.TextInput(attrs = {'class': 'titlefield form-control'}),
            'price': forms.NumberInput(attrs = {'class': 'pricefield form-control', 'placeholder': "가격(원)을 입력해주세요"}),
            # 'category': forms.NumberInput(att rs = {'class': 'categoryfield form-control'}),
        }

        labels = {
            'title': "제목",
            # 'proceeding': "진행상황",
            'price': "가격",
            "contents": "상세 설명",
            # 'category': "카테고리"
        }

