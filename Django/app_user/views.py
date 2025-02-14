from django.shortcuts import render

# 메인 페이지
def user_index(request):
    return render(request, 'index.html', {
        'places': [0, 0, 0, 0, 0, 0, 0, 0, 0]
    })

# 로그인 페이지
def user_login(request):
    return render(request, 'login.html')

# 회원가입 페이지
def user_signup(request):
    return render(request, 'signup.html')

# 계정 찾기 페이지
def user_find(request):
    return render(request, 'find.html')

# 비밀번호 초기화 페이지
def user_reset(request):
    return render(request, 'reset.html')

# 프로필
def user_profile(request):
    return render(request, 'profile.html')

# 이용약관
def user_terms(request):
    return render(request, 'terms.html')

# 연락처
def user_contact(request):
    return render(request, 'contact.html')