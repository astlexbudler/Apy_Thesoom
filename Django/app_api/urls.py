

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

    # 장소 수정 API
    path('update_place', a.update_place, name='update_place'),

    # 장소 삭제 API
    path('delete_place', a.delete_place, name='delete_place'),

    # 장소 이미지 등록 API
    path('create_place_image', a.create_place_image, name='create_place_image'),

    # 장소 이미지 삭제 API
    path('delete_place_image', a.delete_place_image, name='delete_place_image'),

    # 장소 아이템 상세 API
    path('get_place_item_detail', a.get_place_item_detail, name='get_place_item_detail'),

    # 장소 상품 등록 API
    path('create_place_item', a.create_place_item, name='create_place_item'),

    # 장소 상품 수정 API
    path('update_place_item', a.update_place_item, name='update_place_item'),

    # 장소 상품 삭제 API
    path('delete_place_item', a.delete_place_item, name='delete_place_item'),

    # 상품 일정 조회 API
    path('get_item_dates', a.get_item_dates, name='get_item_dates'),

    # 장소 상품 날짜 등록 API
    path('create_item_date', a.create_item_date, name='create_item_date'),

    # 장소 상품 날짜 삭제 API
    path('delete_item_date', a.delete_item_date, name='delete_item_date'),

]
