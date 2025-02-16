from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

from app_core.daos import find_account
from app_core.models import ACCOUNT
from .forms import CustomUserCreationForm, CustomUserFindForm


# 메인 페이지
def user_index(request):
    context = {
        'places': [0, 0, 0, 0, 0, 0, 0, 0, 0]
    }

    if request.user.is_authenticated:
        current_user = get_object_or_404(ACCOUNT, username=request.user)

        context['user'] = current_user

    return render(request, 'index.html', context)

# 로그인 페이지
def user_login(request):
    signup_success = request.session.get('signup_success', False)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        form.error_messages = {
            'invalid_login': _(
                '계정 정보가 일치하지 않습니다.'
            ),
            'inactive': _('휴면 계정입니다.'),
        }

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('user_index')
    else:
        print(signup_success, type(signup_success))
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form, 'signup_success': signup_success})

# 로그아웃
def user_logout(request):
    logout(request)
    return redirect('user_login')

# 회원가입 페이지
def user_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            request.session['signup_success'] = True

            return redirect('user_login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

# 계정 찾기 페이지
def user_find(request):
    form = CustomUserFindForm(request.POST or None)
    user_exist = False
    context = {
        'form': form,
        'user_exist': user_exist,
    }

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        user_exist = find_account(username)

        context = {
            'form': form,
            'user_exist': user_exist,
        }

        if user_exist:
            return redirect('user_reset')
        else:
            return render(request, 'reset.html', context)

    return render(request, 'find.html', context)

# 비밀번호 초기화 페이지
def user_reset(request):
    return render(request, 'reset.html')

# 프로필
@login_required
def user_profile(request):
    return render(request, 'profile.html')

# 이용약관
def user_terms(request):
    return render(request, 'terms.html')

# 연락처
def user_contact(request):
    return render(request, 'contact.html')