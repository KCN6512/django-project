from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана' #все это для того чтобы переименовать пустой параметр

    cat = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),label='Категория',required=False)#сделать категория необязательной
    is_published = forms.BooleanField(initial=False, label='Опубликовать сразу')

    class Meta:
        model = Actor
        fields = ['title', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),

        }

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput())


class DeleteActorForm(forms.Form):
    captcha = CaptchaField()

class TestForm(forms.Form):
    name = forms.CharField()
    browser = forms.CharField()
    comment = forms.CharField()