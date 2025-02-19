from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_core.models import ACCOUNT
from django.utils.translation import gettext_lazy as _
import re

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


class CustomPasswordResetForm(forms.Form):
    password1 = forms.CharField(
        label="새 비밀번호",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="8자 이상, 영문자와 숫자를 모두 포함해서 입력하세요."
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="위와 동일한 비밀번호를 입력하세요."
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
            if len(password1) < 8:
                raise forms.ValidationError("비밀번호는 8자 이상이어야 합니다.")
            # 영문자와 숫자가 모두 포함되었는지 체크
            if not re.search(r'[A-Za-z]', password1) or not re.search(r'[0-9]', password1):
                raise forms.ValidationError("비밀번호는 영문자와 숫자를 모두 포함해야 합니다.")
        return cleaned_data


class CustomUserProfileForm(forms.ModelForm):


    class Meta:
        model = ACCOUNT
        fields = ('username', 'first_name', 'contact')