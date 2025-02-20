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
            # 영문자와 숫자가 모두 포함되었는지 체크
            if not re.search(r'[A-Za-z]', password1) or not re.search(r'[0-9]', password1):
                raise forms.ValidationError("Password must contain a combination of letters and numbers.")
        return cleaned_data


class CustomUserProfileForm(forms.ModelForm):


    class Meta:
        model = ACCOUNT
        fields = ('username', 'first_name', 'contact')