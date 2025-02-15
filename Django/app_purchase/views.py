from django.shortcuts import render

# 결제 요청 페이지
def purchase_request(request):
    return render(request, 'purchase/request.html')

# 결제 완료 페이지
def purchase_complete(request):
    return render(request, 'purchase/complete.html')

# 결제 기록 확인 페이지
def purchase_history(request):
    return render(request, 'purchase/history.html')