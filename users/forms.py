from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Link
from django.core.validators import RegexValidator


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Имя пользователя',
        required=True,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
        validators=[RegexValidator(
            regex=r'^[\w.@+-_]+$',
            message='Введите допустимое имя пользователя. Это значение может содержать только буквы, цифры и @/./+/-/_ символы.',
            code='invalid_username'
        )],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Имя пользователя',
        required=True,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
        validators=[RegexValidator(
            regex=r'^[\w.@+-_]+$',
            message='Введите допустимое имя пользователя. Это значение может содержать только буквы, цифры и @/./+/-/_ символы.',
            code='invalid_username'
        )],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class LinksForm(forms.ModelForm):
    link1 = forms.CharField(
        label='Длинная ссылка',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ссылку'})
    )
    link2 = forms.CharField(
        label='Сокращенная ссылка',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите слово сокращение'})
    )

    def clean_link1(self):
        link1 = self.cleaned_data['link1']
        return link1

    def clean_link2(self):
        link2 = self.cleaned_data['link2']
        return link2

    class Meta:
        model = Link
        fields = ['link1', 'link2']