

from django.urls import path
from . import views as v


urlpatterns = [

    # 메인 페이지
    path('', v.user_index, name='user_index'),

    # 로그인 페이지
    path('login', v.user_login, name='user_login'),

    # 회원가입 페이지
    path('signup', v.user_signup, name='user_signup'),

    # 계정 찾기 페이지
    path('find', v.user_find, name='user_find'),

    # 비밀번호 초기화 페이지
    path('reset', v.user_reset, name='user_reset'),

    # 프로필
    path('profile', v.user_profile, name='user_profile'),

    # 이용약관
    path('terms', v.user_terms, name='user_terms'),

    # 연락처
    path('contact', v.user_contact, name='user_contact'),

]