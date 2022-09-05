from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class MyForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
