from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_core.models import ACCOUNT
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    """
    회원 생성 폼입니다.
    """

    error_messages = {
        "password_mismatch": _("비밀번호가 일치하지 않습니다."),
    }

    class Meta:
        model = ACCOUNT
        fields = ('username', 'password1', 'password2', 'first_name', 'contact')


class CustomUserFindForm(forms.Form):
    username = forms.EmailField(
        widget= forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': '이메일'
        }),
    )