from django import forms
from django.contrib.auth.forms import AuthenticationForm ,UsernameField ,UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}))

    
    
    
class CustemRegistrationForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        
        fields = ['username','email','password1','password2']
        
        
        
        
        
        
        
        
        
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label=' username',widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(label='Email ',widget=forms.EmailInput(attrs={'autofocus':'True','class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)