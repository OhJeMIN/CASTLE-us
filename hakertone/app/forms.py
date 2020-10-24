from django import forms
from .models import Group_buying, Flee_market


class Group_buyingPost(forms.ModelForm):
    class Meta:
        model = Group_buying
        fields = ['title', 'contents']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'titlefield form-control'}),
        }
        labels = {
            'title': "제목",
            'contents': "내용",
        }

    

class Flee_marketPost(forms.ModelForm):
    class Meta:
        model = Flee_market
        fields = ['price','title', 'contents']
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'titlefield form-control'}),
            'price': forms.NumberInput(attrs = {'class': 'pricefield form-control', 'placeholder': "가격(원)을 입력해주세요"}),
        }

        labels = {
            'title': "제목",
            'price': "가격",
            "contents": "상세 설명",
        }

