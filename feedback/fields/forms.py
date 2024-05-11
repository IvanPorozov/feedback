
from django import forms
from django.core.validators import RegexValidator
from captcha.fields import CaptchaField


class AddRecordForm(forms.Form):
    username = forms.CharField(label='User Name', validators=[RegexValidator(r'^[a-zA-Z0-9]+$')], required=True)
    email = forms.EmailField(label='E-mail', required=True)
    homepage = forms.URLField(label='Home Page', required=False)
    captcha = CaptchaField(label='CAPTCHA', required=True)
    text = forms.CharField(label='Text', widget=forms.Textarea, required=True)
    parent_comment_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
