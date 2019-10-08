from django import forms
from django.contrib.auth.models import User
from.models import Post


class Register(forms.ModelForm):
    username=forms.CharField(max_length=100, label='Username')
    first_name=forms.CharField(max_length=100,label='First Name')
    last_name=forms.CharField(max_length=100,label='Last Name')
    password1=forms.CharField(widget=forms.PasswordInput(),label='Password',min_length=8)
    password2=forms.CharField(widget=forms.PasswordInput(),label='Confirm Password', min_length=8)
    
    class Meta:
        model= User
        fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        
    def clean_username(self):
        cd= self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('This username allready registered before ...')
        return cd['username']
    
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password not confirmed...')
        return cd['password2']
    
    
    
class Login(forms.ModelForm):
    username=forms.CharField(max_length=100,label='Username')
    password=forms.CharField(min_length=8,widget=forms.PasswordInput(), label='Password')
    class Meta:
        model= User
        fields= ('username', 'password')
        
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ('post_title', 'name', 'email', 'post_body')