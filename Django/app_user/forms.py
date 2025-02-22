from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_core.models import ACCOUNT
from django.utils.translation import gettext_lazy as _
import re

class CustomUserCreationForm(UserCreationForm):
    # 회원 생성 폼입니다.

    error_messages = {
        "password_mismatch": _("Passwords do not match."),
    }

    class Meta:
        model = ACCOUNT
        # username=이메일, password1=비밀번호, password2=비밀번호 확인, first_name=이름, contact=연락처
        fields = ('username', 'password1', 'password2', 'first_name', 'contact')


class CustomUserFindForm(forms.Form):
    username = forms.EmailField(
        widget= forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
        }),
    )


class CustomPasswordResetForm(forms.Form):
    password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Enter your new password. It must be at least 8 characters long and contain a combination of letters and numbers."
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Re-enter your new password for confirmation."
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords do not match.")
            if len(password1) < 8:
                raise forms.ValidationError("Password must be at least 8 characters long")
            # 영문자와 숫자와 특수문자가 모두 포함되어야 함
            #if not re.search(r'[A-Za-z]', password1) or not re.search(r'[0-9]', password1): # 영문자와 숫자 추가
            if not re.search(r'[A-Za-z0-9]', password1) or not re.search(r'[!@#$%^&*()_+]', password1): # 특수문자 추가
                raise forms.ValidationError("Password must contain a combination of letters and numbers.")
        return cleaned_data


class CustomUserChangeForm(forms.ModelForm):
    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    contact = forms.CharField(
        label="Contact",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = ACCOUNT
        fields = ('first_name', 'contact')