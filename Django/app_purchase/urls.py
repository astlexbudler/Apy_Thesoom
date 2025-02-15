

from django.urls import path
from . import views as v


urlpatterns = [

    # 결제 요청 페이지
    # /purchase/request?item_id=상품ID로 특정 상품 정보를 가져와서 결제 요청 페이지를 표시.
    # 결제하는 상품 정보를 표시하고, 상품의 캘린더를 표시해주는 모달을 띄우는 버튼이 있어야함.
    # 결제에는 예약 시작 날짜와 종료 일시, 요청 사항을 입력할 수 있는 폼이 있어야함.
    # 알리페이 테스트 결제 버튼이 있어야함. 알리페이 테스트 결제 버튼을 누르면, 결제 완료 페이지로 이동.
    # 필요에따라 결제 수단이나 카드 정보 입력 폼을 추가해도 됨. 불필요할 경우 해당 부분은 생략 가능.(가끔 현금 영수증 요청 checkbox 같은 elements를 만들어야하는 경우도 있어서..)
    # 필요할 경우 추가적인 API를 구성. 결제 완료 페이지로 이동할 때, 결제 정보를 넘겨주어야함.
    path('request', v.purchase_request, name='purchase_request'),

    # 결제 완료 페이지
    # 결제 처리 결과에 따라 간단하게 결제 성공, 결제 실패 페이지를 표시.
    # 결제 완료의 경우, 결제한 상품의 정보와 사용자 요청 사항을 표시.(예약 일시, 종료 일시, 요청사항)
    # 결제 실패의 경우, 실패 사유 또는 에러 코드를 표시.
    path('complete', v.purchase_complete, name='purchase_complete'),

    # 결제 기록 확인 페이지
    # 결제한 상품들의 리스트를 표시. 상품 이미지, 상품 이름, 상품 설명, 결제 일시, 결제 상태를 표시.
    # 결제 상태는 결제 완료, 결제 취소, 결제 실패로 구분.
    # 추가적인 내용을 알려주는 modal이나 페이지는 불필요. 해당 페이지에 목록에서 모든 정보를 확인할 수 있어야함.
    path('history', v.purchase_history, name='purchase_history'),

]