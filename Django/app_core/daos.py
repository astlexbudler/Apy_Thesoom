import math
from app_core import models as mo
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import datetime
from django.contrib.auth import get_user_model

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
# get_item_dates(item_id): 아이템 일정 조회
# create_item_date(item_id, year, month, date, content): 아이템 일정 생성
# delete_item_date(item_date_id): 아이템 일정 삭제
# create_purchase(item_id, book_start_datetime, book_end_datetime, payment_agency, payment_method, payment_info, memo=''): 구매 생성
# update_purchase_status(purchase_id, status): 구매 상태 변경
# get_purchases(account_id): 구매 정보 조회

User = get_user_model()

# 사용자 계정 정보 조회
def get_account(account_id):

    # account_id: 사용자 아이디(username)

    account = User.objects.filter(username=account_id).first()
    if not account:
        return None

    return {
        'id': account_id,
        'name': account.first_name,
        'contact': account.contact,
        'is_superuser': account.is_superuser,
    }


# 아이디 찾기
def find_account(username):
    return User.objects.filter(username=username).exists()

# 아이디 중복 확인
def check_account(account_id):

    # account_id: 사용자 아이디(username)
    result = User.objects.get(username=account_id)

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
def search_places(search_keyword, place_status):

    # search_keyword: 검색어(장소 이름)
    # models.filter를 이용해서 쿼리 작성
    # 대표 이미지는 PLACE_IMAGE 테이블에서 image_type='main'인 이미지를 사용

    plaecs = mo.PLACE.objects.filter(
        name__icontains=search_keyword,
        status__in=place_status
    )

    return [{
        'id': place.id,
        'name': place.name,
        'location': place.location,
        'avg_rate': math.ceil(sum([place_review.rate for place_review in mo.REVIEW.objects.filter(place=place)]) / len(mo.REVIEW.objects.filter(place=place))) if mo.REVIEW.objects.filter(place=place) else 0,
        'main_images': [place_main_image.image.url for place_main_image in mo.PLACE_IMAGE.objects.filter(place=place, image_type='main')],
        'status': place.status,
        'discount_from_price': place.discount_from_price,
        'final_from_price': place.final_from_price,
    } for place in plaecs]

# 장소 세부 내용 확인
def get_place_detail(place_id):

    # place_id: 장소 아이디
    # models.get을 이용해서 쿼리 작성
    # PLACE_IMAGE 테이블에서 image_type='main'인 이미지를 사용
    # related_places는 그냥 랜덤으로 6개의 place를 넣도록 함

    place = mo.PLACE.objects.get(id=place_id)
    place_main_images = mo.PLACE_IMAGE.objects.filter(place=place, image_type='main')
    place_sub_images = mo.PLACE_IMAGE.objects.filter(place=place, image_type='sub')
    place_items = mo.PLACE_ITEM.objects.filter(place=place)
    place_reviews = mo.REVIEW.objects.select_related('author').filter(place=place)
    place_related_places = mo.PLACE.objects.filter(status='active').order_by('?')[:6]
    avg_rate = math.ceil(sum([place_review.rate for place_review in place_reviews]) / len(place_reviews)) if place_reviews else 0

    return {
        'id': place.id,
        'name': place.name,
        'intro': place.intro,
        'location': place.location,
        'location_link': place.location_link,
        'description': place.description,
        'discount_from_price': place.discount_from_price,
        'final_from_price': place.final_from_price,
        'status': place.status,
        'main_images': [{
            'id': place_main_image.pk,
            'image': place_main_image.image.url,
        } for place_main_image in place_main_images],
        'sub_images': [{
            'id': place_sub_image.pk,
            'image': place_sub_image.image.url,
        } for place_sub_image in place_sub_images],
        'items': [{
            'id': place_item.pk,
            'name': place_item.name,
            'description': place_item.description,
            'price': place_item.price,
            'image': place_item.image.url,
            'dates': [{
                'id': place_item_date.pk,
                'year': place_item_date.year,
                'month': place_item_date.month,
                'date': place_item_date.date,
                'content': place_item_date.content,
            } for place_item_date in mo.ITEM_DATE.objects.filter(item=place_item)],
        } for place_item in place_items],
        'avg_rate': avg_rate,
        'reviews': [{
            'id': place_review.pk,
            'author_name': place_review.author.first_name,
            'rate': place_review.rate,
            'content': place_review.content,
            'image': '/media/' + str(place_review.images) if place_review.images else None,
            'created_at': place_review.created_at,
        } for place_review in place_reviews],
        'related_places': [{
            'id': place_related_place.id,
            'name': place_related_place.name,
            'location': place_related_place.location,
            'avg_rate': math.ceil(sum([place_review.rate for place_review in mo.REVIEW.objects.filter(place=place_related_place)]) / len(mo.REVIEW.objects.filter(place=place_related_place))) if mo.REVIEW.objects.filter(place=place_related_place) else 0,
            'main_images': [place_related_main_image.image.url for place_related_main_image in mo.PLACE_IMAGE.objects.filter(place=place_related_place, image_type='main')],
            'status': place_related_place.status,
            'discount_from_price': 300,
            'final_from_price': 200,
        } for place_related_place in place_related_places],
    }

# 새 장소 등록
def create_place():

    # name: 장소 이름
    # intro: 짧은 소개
    # location: 장소
    # location_link: 장소 링크
    # description: 소개(html)
    # status: 상태

    # models.create를 이용해서 쿼리 작성

    try:
        place = mo.PLACE.objects.create(
            name='name',
            intro='short intro description',
            location='location info',
            location_link='map location link',
            description='<h1>Please write description here.</h1>',
            status='writing',
            discount_from_price=300,
            final_from_price=200
        )
        return {
            'success': True,
            'place_id': place.id,
            'message': 'Place created successfully.',
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
        }

# 장소 수정
def update_place(place_id, name, intro, location, location_link, description, discount_from_price, final_from_price, place_status):

    # place_id: 장소 아이디
    # name: 장소 이름
    # intro: 짧은 소개
    # location: 장소
    # location_link: 장소 링크
    # description: 소개(html)
    # status: 상태

    # models.update를 이용해서 쿼리 작성
    place = mo.PLACE.objects.get(id=place_id)
    place.name = name
    place.intro = intro
    place.location = location
    place.location_link = location_link
    place.description = description
    place.discount_from_price = discount_from_price
    place.final_from_price = final_from_price
    place.status = place_status
    place.save()

    return {
        'success': True,
        'message': 'Place updated successfully.',
    }


# 장소 삭제
def delete_place(place_id):

    # place_id: 장소 아이디

    # models.delete를 이용해서 쿼리 작성
    try:
        place = mo.PLACE.objects.get(id=place_id)
        place.delete()
        return {
            'success': True,
            'message': 'Place deleted successfully.',
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
        }

# 장소 이미지 등록
def create_place_image(place_id, image, image_type):

    # place_id: 장소 아이디
    # image: 이미지
    # image_type: 이미지 타입

    # models.create를 이용해서 쿼리 작성
    try:
        place = mo.PLACE.objects.get(id=place_id)
        place_image = mo.PLACE_IMAGE.objects.create(
            place=place,
            image=image,
            image_type=image_type,
        )
        return {
            'success': True,
            'message': 'Place image created successfully.',
            'image_id': place_image.pk,
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
        }

# 장소 이미지 삭제
def delete_place_image(image_id):

    # image_id: 이미지 아이디

    # models.delete를 이용해서 쿼리 작성
    try:
        place_image = mo.PLACE_IMAGE.objects.get(id=image_id)
        place_image.delete()
        return {
            'success': True,
            'message': 'Place image deleted successfully.',
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
        }

# 장소 아이템 상세
def get_place_item_detail(item_id):

    # item_id: 아이템 아이디
    # models.get을 이용해서 쿼리 작성
    # ITEM_DATE 테이블에서 아이템 아이디로 필터링

    try:
        item = mo.PLACE_ITEM.objects.get(id=item_id)
        item_dates = mo.ITEM_DATE.objects.filter(item=item)

        item_dates_list = [{
            'id': item_date.pk,
            'year': item_date.year,
            'month': item_date.month,
            'date': item_date.date,
            'content': item_date.content,
        } for item_date in item_dates]

        return {
            'id': item.pk,
            'name': item.name,
            'description': item.description,
            'price': item.price,
            'image': item.image.url,  # 이미지 URL을 반환
            'item_dates': item_dates_list
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
        }

# 장소 아이템 생성
def create_place_item(place_id, name, description, price, image):

    # place_id: 장소 아이디
    # name: 상품 이름
    # description: 설명(html)
    # price: 가격

    # models.create를 이용해서 쿼리 작성
    try:
        place = mo.PLACE.objects.get(id=place_id)
        item = mo.PLACE_ITEM.objects.create(
            place=place,
            name=name,
            description=description,
            price=price,
            image=image
        )
        return {
            'success': True,
            'message': 'Place item created successfully.',
            'item_id': item.pk,
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
        }

# 장소 아이템 수정
def update_place_item(item_id, name=None, description=None, price=None):

    # item_id: 아이템 아이디
    # name: 상품 이름
    # description: 설명(html)
    # price: 가격

    # models.update를 이용해서 쿼리 작성
    try:
        item = mo.PLACE_ITEM.objects.get(id=item_id)
        if name:
            item.name = name
        if description:
            item.description = description
        if price:
            item.price = price
        item.save()
        return {
            'success': True,
            'message': 'Place item updated successfully.',
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
        }

# 장소 아이템 삭제
def delete_place_item(item_id):

    # item_id: 아이템 아이디

    # models.delete를 이용해서 쿼리 작성
    try:
        item = mo.PLACE_ITEM.objects.get(id=item_id)
        item.delete()
        return {
            'success': True,
            'message': 'Place item deleted successfully.',
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
        }

# 리뷰 작성
def create_review(place_id, account_id, rate, content, image):

    # place_id: 장소 아이디
    # rate: 평점(1~5)
    # content: 내용
    # images: 이미지(리스트)

    # models.create를 이용해서 쿼리 작성
    review = mo.REVIEW.objects.create(
        place= mo.PLACE.objects.get(id=place_id),
        author= User.objects.get(id=account_id),
        rate=rate,
        content=content,
        images=image
    )

    return {
        'success': True,
        'review_id': review.pk,
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

# 아이템 일정 조회
def get_item_dates(item_id):

    # item_id: 아이템 아이디

    # 이번달만
    this_month = datetime.datetime.now().month
    dates = mo.ITEM_DATE.objects.filter(item_id=item_id, month=this_month)

    return [{
        'id': date.pk,
        'year': date.year,
        'month': date.month,
        'date': date.date,
        'content': date.content,
    } for date in dates]


# 아이템 일정 생성
def create_item_date(item_id, year, month, date, content):

    # item_id: 아이템 아이디
    # year: 연도
    # month: 월
    # date: 날짜
    # content: 표시할 내용

    # 이미 해당 날짜에 일정이 있는 경우 스킵
    if mo.ITEM_DATE.objects.filter(item_id=item_id, year=year, month=month, date=date).exists():
        return {
            'success': False,
            'message': 'Item date already exists.',
        }

    # models.create를 이용해서 쿼리 작성
    item = mo.PLACE_ITEM.objects.get(id=item_id)
    item_date = mo.ITEM_DATE.objects.create(
        item=item,
        year=year,
        month=month,
        date=date,
        content=content
    )
    return {
        'success': True,
        'message': 'Item date created successfully.',
        'item_date_id': item_date.pk,
    }

# 아이템 일정 삭제
def delete_item_date(item_date_id):

    # item_date_id: 아이템 일정 아이디

    # models.delete를 이용해서 쿼리 작성
    try:
        item_date = mo.ITEM_DATE.objects.get(id=item_date_id)
        item_date.delete()
        return {
            'success': True,
            'message': 'Item date deleted successfully.',
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
        }

# 구매 생성
def create_purchase(account_id, item_id, book_start_datetime, book_end_datetime, payment_agency, payment_method, payment_info, memo=''):

    # item_id: 아이템 아이디
    # book_start_datetime: 예약 시작 일시
    # book_end_datetime: 예약 종료 일시
    # payment_agency: 결제사
    # payment_method: 결제 방법
    # payment_info: 결제 정보(json)
    # memo: 요청 사항

    mo.PURCHASE.objects.create(
        account_id=account_id,
        item_id=item_id,
        book_start_datetime=book_start_datetime,
        book_end_datetime=book_end_datetime,
        payment_agency=payment_agency,
        payment_method=payment_method,
        payment_info=payment_info,
        memo=memo,
        status='completed'
    )

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

    purchase = mo.PURCHASE.objects.select_related('item').select_related('item__place').filter(account_id=account_id)

    return [{
        'id': purchase.pk,
        'place': {
            'id': purchase.item.place.pk,
            'name': purchase.item.place.name,
        },
        'item': {
            'id': purchase.item.pk,
            'name': purchase.item.name,
            'description': purchase.item.description,
            'price': purchase.item.price,
            'image': '/media/' + str(purchase.item.image) if purchase.item.image else None,
        },
        'book_start_datetime': datetime.datetime.strftime(purchase.book_start_datetime, '%Y-%m-%d'),
        'book_end_datetime': datetime.datetime.strftime(purchase.book_end_datetime, '%Y-%m-%d'),
        'memo': purchase.memo,
        'created_at': purchase.created_at,
        'purchase_at': purchase.purchase_at,
        'payment_agency': purchase.payment_agency,
        'payment_method': purchase.payment_method,
        'payment_info': purchase.payment_info,
        'status': purchase.status,
    } for purchase in purchase]
