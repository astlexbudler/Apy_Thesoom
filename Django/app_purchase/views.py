import datetime
from django.shortcuts import render, redirect
from app_core import daos
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# 결제 요청 페이지
@csrf_exempt
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

    # 결제 요청 처리
    if request.method == 'POST':
        # 결제 요청 처리
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        memo = request.POST.get('memo')

        daos.create_purchase(request.user.id, item_id, start_date, end_date, 'alipay', 'card', '{}', memo)

        # 예약된 날짜에 'No Vacancy' 추가
        start_datetime = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_datetime = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        for i in range((end_datetime - start_datetime).days + 1):
            daos.create_item_date(
                item_id=item_id,
                year=int((start_datetime + datetime.timedelta(days=i)).strftime('%Y')),
                month=int((start_datetime + datetime.timedelta(days=i)).strftime('%m')),
                date=int((start_datetime + datetime.timedelta(days=i)).strftime('%d')),
                content='No Vacancy'
            )

        return JsonResponse({'result': 'success'})

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
    print(purchases)

    return render(request, 'purchase/history.html', {
        'purchases': purchases
    })