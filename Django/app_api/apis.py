from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from app_core import models as mo
from app_core import daos as do
from django.views.decorators.csrf import csrf_exempt

# 로그인 API
def api_login(request):
    return JsonResponse({'result': 'success'})

# 로그아웃 API
def api_logout(request):
    return JsonResponse({'result': 'success'})

# 회원 API
def api_account(request):
    return JsonResponse({'result': 'success'})

# 리뷰 API
# POST: 리뷰 작성
# DELETE: 리뷰 삭제
def api_review(request):

    if request.method == 'POST':
        # 요청 데이터 가져오기
        place_id = request.POST.get('place_id')
        review = do.create_review(
            place_id=place_id,
            account_id=request.user.id,
            rate=request.POST.get('rate'),
            content=request.POST.get('content'),
            image= request.FILES.get('image'),
        )

        if not review['success']:
            return JsonResponse({
                'success': False,
                'message': review['message'],
            }, status=400)

        return JsonResponse({
            'success': True,
            'message': 'Review created successfully',
        })

    elif request.method == 'DELETE':
        # 요청 데이터 가져오기
        review_id = request.POST.get('review_id')
        if not review_id:
            return JsonResponse({'success': False, 'message': 'review_id is required'}, status=400)

        delete_review = do.delete_review(review_id)

        if not delete_review['success']:
            return JsonResponse({
                'success': False,
                'message': delete_review['message'],
            }, status=400)

        return JsonResponse({
            'success': True,
            'message': 'Review deleted successfully',
        })

    return JsonResponse({'result': 'success'})

# 장소 API
def api_place(request):


    if request.method == 'DELETE':
        # 요청 데이터 가져오기
        place_id = request.GET.get('place_id')
        if not place_id:
            return JsonResponse({'success': False, 'message': 'place_id is required'}, status=400)

        delete_place = do.delete_place(place_id)

        if not delete_place['success']:
            return JsonResponse({
                'success': False,
                'message': delete_place['message'],
            }, status=400)

        return JsonResponse({
            'success': True,
            'message': 'Place deleted successfully',
        })

    return JsonResponse({'result': 'success'})

# 장소 수정 API
@ csrf_exempt
def update_place(request):
    if request.method == 'POST':

        # 요청 데이터 가져오기
        place_id = request.POST.get('place_id')
        if not place_id:
            return JsonResponse({'success': False, 'message': 'place_id is required'}, status=400)

        update_place = do.update_place(
            place_id=place_id,
            name=request.POST.get('name'),
            intro=request.POST.get('intro'),
            location=request.POST.get('location'),
            location_link=request.POST.get('location_link'),
            description=request.POST.get('description'),
            discount_from_price=request.POST.get('discount_from_price'),
            final_from_price=request.POST.get('final_from_price'),
            place_status=request.POST.get('status'),
        )
        print(update_place)

        if not update_place['success']:
            return JsonResponse({
                'success': False,
                'message': update_place['message'],
            }, status=400)

        return JsonResponse({
            'success': True,
            'message': 'Place updated successfully',
        })

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

# 장소 삭제 API
@ csrf_exempt
def delete_place(request):
    if request.method == 'DELETE':
        try:
            # 요청 데이터 가져오기
            place_id = request.POST.get('place_id')
            if not place_id:
                return JsonResponse({'success': False, 'message': 'place_id is required'}, status=400)

            delete_place = do.delete_place(place_id)

            if not delete_place['success']:
                return JsonResponse({
                    'success': False,
                    'message': delete_place['message'],
                }, status=400)

            return JsonResponse({
                'success': True,
                'message': 'Place deleted successfully',
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e),
            }, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

# 장소 이미지 등록 API
@ csrf_exempt
def create_place_image(request):
    if request.method == 'POST':

        # 요청 데이터 가져오기
        place_id = request.POST.get('place_id')
        if not place_id:
            return JsonResponse({'success': False, 'message': 'place_id is required'}, status=400)

        # 이미지 파일들 가져오기
        images = request.FILES.getlist('images')
        image_type = request.POST.get('image_type')

        # 이미지 순서 가져오기
        print('images:', images)
        for image in images:
            print('image:', image)
            do.create_place_image(
                place_id=place_id,
                image=image,
                image_type=image_type,
            )


        return JsonResponse({
            'success': True,
            'message': 'Place images created successfully',
        })


    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

# 장소 이미지 삭제 API
@csrf_exempt
def delete_place_image(request):

    # 요청 데이터 가져오기
    image_id = request.POST.get('image_id')
    if not image_id:
        return JsonResponse({'success': False, 'message': 'image_id is required'}, status=400)

    delete_place_image = do.delete_place_image(image_id)

    if not delete_place_image['success']:
        return JsonResponse({
            'success': False,
            'message': delete_place_image['message'],
        }, status=400)

    return JsonResponse({
        'success': True,
        'message': 'Place image deleted successfully',
    })

# 장소 아이템 상세 API
@ csrf_exempt
def get_place_item_detail(request):
    if request.method == 'GET':
        try:
            # 요청 데이터 가져오기
            item_id = request.GET.get('item_id')
            if not item_id:
                return JsonResponse({'success': False, 'message': 'item_id is required'}, status=400)

            place_item = do.get_place_item_detail(item_id)

            if not place_item['success']:
                return JsonResponse({
                    'success': False,
                    'message': place_item['message'],
                }, status=400)

            return JsonResponse({
                'success': True,
                'message': 'Place item detail',
                'item': place_item['item'],
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e),
            }, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

# 장소 상품 등록 API
@ csrf_exempt
def create_place_item(request):
    if request.method == 'POST':

        # 요청 데이터 가져오기
        place_id = request.POST.get('place_id')
        if not place_id:
            return JsonResponse({'success': False, 'message': 'place_id is required'}, status=400)

        add_place_item = do.create_place_item(
            place_id=place_id,
            image=request.FILES.get('image'),
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
        )

        if not add_place_item['success']:
            return JsonResponse({
                'success': False,
                'message': add_place_item['message'],
            }, status=400)

        return JsonResponse({
            'success': True,
            'message': 'Place item added successfully',
            'item_id': add_place_item['item_id'],
        })


    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

# 장소 상품 수정 API
@ csrf_exempt
def update_place_item(request):
    if request.method == 'POST':
        try:
            # 요청 데이터 가져오기
            item_id = request.POST.get('item_id')
            if not item_id:
                return JsonResponse({'success': False, 'message': 'item_id is required'}, status=400)

            edit_place_item = do.edit_place_item(
                item_id=item_id,
                image=request.FILES.get('image'),
                name=request.POST.get('name'),
                description=request.POST.get('description'),
                price=request.POST.get('price'),
            )

            if not edit_place_item['success']:
                return JsonResponse({
                    'success': False,
                    'message': edit_place_item['message'],
                }, status=400)

            return JsonResponse({
                'success': True,
                'message': 'Place item updated successfully',
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e),
            }, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

# 장소 상품 삭제 API
@ csrf_exempt
def delete_place_item(request):
    if request.method == 'DELETE':
        try:
            # 요청 데이터 가져오기
            item_id = request.POST.get('item_id')
            if not item_id:
                return JsonResponse({'success': False, 'message': 'item_id is required'}, status=400)

            delete_place_item = do.delete_place_item(item_id)

            if not delete_place_item['success']:
                return JsonResponse({
                    'success': False,
                    'message': delete_place_item['message'],
                }, status=400)

            return JsonResponse({
                'success': True,
                'message': 'Place item deleted successfully',
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e),
            }, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

# 상품 일정 조회 API
@ csrf_exempt
def get_item_dates(request):
    if request.method == 'GET':
        try:
            # 요청 데이터 가져오기
            item_id = request.GET.get('item_id')
            if not item_id:
                return JsonResponse({'success': False, 'message': 'item_id is required'}, status=400)

            item_dates = do.get_item_dates(item_id)

            if not item_dates['success']:
                return JsonResponse({
                    'success': False,
                    'message': item_dates['message'],
                }, status=400)

            return JsonResponse({
                'success': True,
                'message': 'Item dates',
                'item_dates': item_dates['item_dates'],
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e),
            }, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

# 상품 일정 등록 API
@ csrf_exempt
def create_item_date(request):
    if request.method == 'POST':
        # 요청 데이터 가져오기
        item_id = request.POST.get('item_id')
        if not item_id:
            return JsonResponse({'success': False, 'message': 'item_id is required'}, status=400)

        full_date = request.POST.get('date') # yyyy-mm-dd
        year = full_date.split('-')[0]
        month = full_date.split('-')[1]
        date = full_date.split('-')[2]

        add_item_date = do.create_item_date(
            item_id=item_id,
            year=year,
            month=month,
            date=date,
            content=request.POST.get('description'),
        )

        if not add_item_date['success']:
            return JsonResponse({
                'success': False,
                'message': add_item_date['message'],
            }, status=400)

        return JsonResponse({
            'success': True,
            'message': 'Item date added successfully',
            'item_date_id': add_item_date['item_date_id'],
        })

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

# 상품 일정 삭제 API
@csrf_exempt
def delete_item_date(request):

    # 요청 데이터 가져오기
    date_id = request.POST.get('date_id')
    if not date_id:
        return JsonResponse({'success': False, 'message': 'date_id is required'}, status=400)

    delete_item_date = do.delete_item_date(date_id)

    if not delete_item_date['success']:
        return JsonResponse({
            'success': False,
            'message': delete_item_date['message'],
        }, status=400)

    return JsonResponse({
        'success': True,
        'message': 'Item date deleted successfully',
    })
