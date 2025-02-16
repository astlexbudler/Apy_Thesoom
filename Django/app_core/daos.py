# 함수 목록
# get_account(account_id): 사용자 계정 정보 조회
# find_account(username): 사용자 조회
# check_account(account_id): 아이디 중복 확인
# create_account(email, password, name): 사용자 계정 정보 생성
# update_account(email, password=None, name=None): 사용자 계정 정보 수정
# delete_account(email): 사용자 계정 정보 삭제
# search_places(search_keyword): 장소 정보 검색
# get_place_detail(place_id): 장소 세부 내용 확인
# create_place(name, intro, location, location_link, description, status): 새 장소 등록
# update_place(place_id, name=None, intro=None, location=None, location_link=None, description=None, status=None): 장소 수정
# delete_place(place_id): 장소 삭제
# create_place_image(place_id, image, image_type, order): 장소 이미지 등록
# delete_place_image(image_id): 장소 이미지 삭제
# get_place_item_detail(item_id): 장소 아이템 상세
# create_place_item(place_id, name, description, price): 장소 아이템 생성
# update_place_item(item_id, name=None, description=None, price=None): 장소 아이템 수정
# delete_place_item(item_id): 장소 아이템 삭제
# create_review(place_id, rate, content, images): 리뷰 작성
# delete_review(review_id): 리뷰 삭제
# create_item_date(item_id, year, month, date, content): 아이템 일정 생성
# delete_item_date(item_date_id): 아이템 일정 삭제
# create_purchase(item_id, book_start_datetime, book_end_datetime, payment_agency, payment_method, payment_info, memo=''): 구매 생성
# update_purchase_status(purchase_id, status): 구매 상태 변경
# get_purchases(account_id): 구매 정보 조회

from django.contrib.auth import get_user_model

User = get_user_model()

# 사용자 계정 정보 조회
def get_account(account_id):

    # account_id: 사용자 아이디(username)

    account = {
        'id': 'applify.kr@gmail.com',
        'name': 'Applify',
        'is_superuser': True,
        'date_joined': '2021-01-01 00:00:00',
        'last_login': '2021-01-01 00:00:00',
    }

    return account

# 아이디 찾기
def find_account(username):
    result = User.objects.filter(username=username).exists()

    return result

# 아이디 중복 확인
def check_account(account_id):

    # account_id: 사용자 아이디(username)
    result = User.objects.get(pk=account_id)

    # models.filter를 이용해서 쿼리 작성

    return {
        'success': result,
        'message': 'Account' + ' ' if result else "don't " + 'exists.',
    }

# 사용자 계정 정보 생성
def create_account(email, password, name):

    # email: 이메일
    # password: 비밀번호
    # name: 이름

    # models.create를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Account created successfully.',
    }

# 사용자 계정 정보 수정
def update_account(email, password=None, name=None):

    # email: 이메일
    # password: 비밀번호
    # name: 이름

    # models.update를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Account updated successfully.',
    }

# 사용자 계정 정보 삭제
def delete_account(email):

    # email: 이메일

    # models.delete를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Account deleted successfully.',
    }

# 장소 정보 검색
def search_places(search_keyword):

    # search_keyword: 검색어(장소 이름)
    # models.filter를 이용해서 쿼리 작성
    # 대표 이미지는 PLACE_IMAGE 테이블에서 image_type='main'인 이미지를 사용

    places = [{
        'id': 1,
        'name': 'The Franklin London – Starhotels Collezione',
        'location': '24 Egerton Gardens, Chelsea, London',
        'avg_rate': 5,
        'main_images': ['/static/img/samples/0.jpg'],
        'status': 'active',
    }]

    return places

# 장소 세부 내용 확인
def get_place_detail(place_id):

    # place_id: 장소 아이디
    # models.get을 이용해서 쿼리 작성
    # PLACE_IMAGE 테이블에서 image_type='main'인 이미지를 사용
    # related_places는 그냥 랜덤으로 6개의 place를 넣도록 함

    place = {
        'id': 1,
        'name': 'The Franklin London – Starhotels Collezione',
        'intro': 'The Franklin London – Starhotels Collezione is a luxury hotel located in the heart of London.',
        'location': '24 Egerton Gardens, Chelsea, London',
        'location_link': 'https://www.google.com/maps?sca_esv=a12588ecf4d7e578&rlz=1C5CHFA_enKR1053KR1053&output=search&q=The+Franklin+London&source=lnms&fbs=ABzOT_CZsxZeNKUEEOfuRMhc2yCI6hbTw9MNVwGCzBkHjFwaK321z773wCjxZUmvDroqphlIJR493mMxNbRCE7CsjxN0zrcX3q5osSt8yM9HtIcApR-qytgB7SnKESLXhABDXCne24GoJWBDR_kZ0la7ZiHwb-YziOH2eZYEdtGI-iMn_X01NPUZMq-6QTrdt__YKLW2sBwX&entry=mc&ved=1t:200715&ictx=111',
        'description': '<h1>The Franklin London – Starhotels Collezione</h1><p>The Franklin London – Starhotels Collezione is a luxury hotel located in the heart of London.</p>',
        'status': 'active',
        'main_images': ['/static/img/samples/0.jpg'],
        'sub_images': ['/static/img/samples/1.jpg'],
        'items': [{
            'id': 1,
            'name': 'Deluxe Room',
            'description': '<h1>Deluxe Room</h1><p>Deluxe Room is a luxury room with a view of the city.</p>',
            'price': 300,
            'image': '/static/img/samples/2.jpg',
        }],
        'avg_rate': 5,
        'reviews': [{
            'id': 1,
            'author_name': 'Applify',
            'rate': 5,
            'content': 'The Franklin London is a great hotel.',
            'images': ['/static/img/samples/3.jpg'],
            'created_at': '2021-01-01 00:00:00',
        }],
        'related_places': [{
            'id': 1,
            'name': 'The Franklin London – Starhotels Collezione',
            'location': '24 Egerton Gardens, Chelsea, London',
            'avg_rate': 5,
            'main_images': ['/static/img/samples/0.jpg'],
            'status': 'active',
        }],
    }

    return place

# 새 장소 등록
def create_place(name, intro, location, location_link, description, status):

    # name: 장소 이름
    # intro: 짧은 소개
    # location: 장소
    # location_link: 장소 링크
    # description: 소개(html)
    # status: 상태

    # models.create를 이용해서 쿼리 작성

    return {
        'success': True,
        'place_id': 1,
        'message': 'Place created successfully.',
    }

# 장소 수정
def update_place(place_id, name=None, intro=None, location=None, location_link=None, description=None, status=None):

    # place_id: 장소 아이디
    # name: 장소 이름
    # intro: 짧은 소개
    # location: 장소
    # location_link: 장소 링크
    # description: 소개(html)
    # status: 상태

    # models.update를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Place updated successfully.',
    }

# 장소 삭제
def delete_place(place_id):

    # place_id: 장소 아이디

    # models.delete를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Place deleted successfully.',
    }

# 장소 이미지 등록
def create_place_image(place_id, image, image_type, order):

    # place_id: 장소 아이디
    # image: 이미지
    # image_type: 이미지 타입
    # order: 이미지 표시 순서

    # models.create를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Place image created successfully.',
    }

# 장소 이미지 삭제
def delete_place_image(image_id):

    # image_id: 이미지 아이디

    # models.delete를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Place image deleted successfully.',
    }

# 장소 아이템 상세
def get_place_item_detail(item_id):

    # item_id: 아이템 아이디
    # models.get을 이용해서 쿼리 작성

    item = {
        'id': 1,
        'name': 'Deluxe Room',
        'description': '<h1>Deluxe Room</h1><p>Deluxe Room is a luxury room with a view of the city.</p>',
        'price': 300,
        'image': '/static/img/samples/2.jpg',
        'item_dates': [{
            'id': 1,
            'year': 2021,
            'month': 1,
            'date': 1,
            'content': 'Deluxe Room is available.',
        }]
    }

    return item

# 장소 아이템 생성
def create_place_item(place_id, name, description, price):

    # place_id: 장소 아이디
    # name: 상품 이름
    # description: 설명(html)
    # price: 가격

    # models.create를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Place item created successfully.',
    }

# 장소 아이템 수정
def update_place_item(item_id, name=None, description=None, price=None):

    # item_id: 아이템 아이디
    # name: 상품 이름
    # description: 설명(html)
    # price: 가격

    # models.update를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Place item updated successfully.',
    }

# 장소 아이템 삭제
def delete_place_item(item_id):

    # item_id: 아이템 아이디

    # models.delete를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Place item deleted successfully.',
    }


# 리뷰 작성
def create_review(place_id, rate, content, images):

    # place_id: 장소 아이디
    # rate: 평점(1~5)
    # content: 내용
    # images: 이미지(리스트)

    # models.create를 이용해서 쿼리 작성

    return {
        'success': True,
        'review_id': 1,
        'message': 'Review created successfully.',
    }

# 리뷰 삭제
def delete_review(review_id):

    # review_id: 리뷰 아이디

    # models.delete를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Review deleted successfully.',
    }

# 아이템 일정 생성
def create_item_date(item_id, year, month, date, content):

    # item_id: 아이템 아이디
    # year: 연도
    # month: 월
    # date: 날짜
    # content: 표시할 내용

    # models.create를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Item date created successfully.',
    }

# 아이템 일정 삭제
def delete_item_date(item_date_id):

    # item_date_id: 아이템 일정 아이디

    # models.delete를 이용해서 쿼리 작성

    return {
        'success': True,
        'message': 'Item date deleted successfully.',
    }

# 구매 생성
def create_purchase(item_id, book_start_datetime, book_end_datetime, payment_agency, payment_method, payment_info, memo=''):

    # item_id: 아이템 아이디
    # book_start_datetime: 예약 시작 일시
    # book_end_datetime: 예약 종료 일시
    # payment_agency: 결제사
    # payment_method: 결제 방법
    # payment_info: 결제 정보(json)
    # memo: 요청 사항

    return {
        'success': True,
        'purchase_id': 1,
        'status': 'pending',
        'message': 'Purchase created successfully.',
    }

# 구매 상태 변경
def update_purchase_status(purchase_id, status):

    # purchase_id: 구매 아이디
    # status: 상태

    return {
        'success': True,
        'message': 'Purchase status updated successfully.',
    }

# 구매 정보 조회
def get_purchases(account_id):

    # account_id: 사용자 아이디

    purchases = [{
        'id': 1,
        'place': {
            'id': 1,
            'name': 'The Franklin London – Starhotels Collezione',
        },
        'item': {
            'id': 1,
            'name': 'Deluxe Room',
            'description': '<h1>Deluxe Room</h1><p>Deluxe Room is a luxury room with a view of the city.</p>',
            'price': 300,
            'image': '/static/img/samples/2.jpg',
        },
        'book_start_datetime': '2021-01-01 00:00:00',
        'book_end_datetime': '2021-01-02 00:00:00',
        'memo': 'Please prepare a birthday cake.',
        'created_at': '2021-01-01 00:00:00',
        'purchase_at': '2021-01-01 00:00:00',
        'payment_agency': 'ALIPAY',
        'payment_method': 'credit card',
        'payment_info': {
            'card_number': '1234-5678-9012-3456',
            'expiration_date': '12/23',
            'cvc': '123',
        },
        'status': 'approved',
    }]

    return purchases