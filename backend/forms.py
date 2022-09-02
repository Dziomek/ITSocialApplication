from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args,**kwargs)

        username = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}),
            label ='Email')

        password = forms.CharField(widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}))

        captcha=ReCaptchaField(widget=ReCaptchaV2Checkbox())