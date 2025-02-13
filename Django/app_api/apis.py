from django.shortcuts import render
from django.http import JsonResponse

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
def api_review(request):
    return JsonResponse({'result': 'success'})

# 장소 API
def api_place(request):
    return JsonResponse({'result': 'success'})
