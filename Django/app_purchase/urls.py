

from django.urls import path
from . import views as v


urlpatterns = [

    # 결제 요청 페이지
    path('request', v.purchase_request, name='purchase_request'),

    # 결제 완료 페이지
    path('complete', v.purchase_complete, name='purchase_complete'),

    # 결제 기록 확인 페이지
    path('history', v.purchase_history, name='purchase_history'),

]