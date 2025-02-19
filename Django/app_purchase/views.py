from django.shortcuts import render, redirect
from app_core import daos

# 결제 요청 페이지
def purchase_request(request):

    # 사용자 정보 확인
    #if not request.user.is_authenticated: # 로그인이 안되어 있을 경우
        #return redirect('/') # 메인 페이지로 이동

    account = daos.get_account(request.user.username)

    # 결제 객실 정보 가져오기
    item_id = request.GET.get('item_id')
    item = daos.get_place_item_detail(item_id)
    #if not item: # 없는 객실 정보일 경우
        #return redirect('/')

    # 객실 예약 정보 확인
    item_dates = daos.get_item_dates(item_id)

    return render(request, 'purchase/request.html', {
        'account': account,
        'item': item,
        'item_dates': item_dates
    })

# 결제 완료 페이지
def purchase_complete(request):
    return render(request, 'purchase/complete.html')

# 결제 기록 확인 페이지
def purchase_history(request):

    # 사용자 정보 확인
    #if not request.user.is_authenticated: # 로그인이 안되어 있을 경우
        #return redirect('/') # 메인 페이지로 이동

    # 결제 기록 가져오기
    purchases = daos.get_purchases(request.user.id)

    return render(request, 'purchase/history.html', {
        'purchases': purchases
    })