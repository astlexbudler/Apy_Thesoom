

from django.urls import path
from . import apis as a


urlpatterns = [

    # 로그인 API
    path('login', a.api_login, name='api_login'), # 로그인 API

    # 로그아웃 API
    # path('logout', a.api_logout, name='api_logout'), # 로그아웃 API

    # 회원 API
    # GET: 회원 정보 검색(아이디로 검색)
    # POST-create: 회원 가입
    # POST-update: 회원 정보 수정
    # DELETE: 회원 탈퇴
    path('account', a.api_account, name='api_account'),

    # 리뷰 API
    # POST-create: 리뷰 작성
    # DELETE: 리뷰 삭제
    path('review', a.api_review, name='api_review'),

    # 장소 API
    # POST-item_date: 장소 상품에 날짜 데이터 추가
    # DELETE-item_date: 장소 상품에 날짜 데이터 삭제
    # POST-image: 장소 이미지 추가
    # DELETE-image: 장소 이미지 삭제
    # POST-item: 장소 상품 추가
    # DELETE-item: 장소 상품 삭제
    path('place', a.api_place, name='api_place'),

]