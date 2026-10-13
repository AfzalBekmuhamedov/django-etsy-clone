from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from blog.models import User,Comment

class SignUpFrom(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"username"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"password again"
    }))

    class Meta:
        model = User
        fields = ['username','password1','password2']

class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "password"
    }))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title']
        widgets = {
            "title":forms.Textarea(attrs={
                "class":"form-control",
                "rows":3
            })
        }