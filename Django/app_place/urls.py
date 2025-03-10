

from django.urls import path
from . import views as v


urlpatterns = [

    # 장소 정보 상세 페이지
    # 상단에 대표 이미지 캐로셀이 있어야함. 이미지는 PLACE_IMAGE 중 PLACE_IMAGE.image_type이 main인 이미지를 사용.
    # 이미지 캐로셀 아래에는 장소 이름, 장소 위치, 장소 소개, 장소 설명이 표시되어야함. 장소 설명은 html로 작성되어서 content|safe 필터를 사용하여 표시.
    # 장소 이름 옆에는 ACCOUNT의 is_superuser가 True인 경우, 장소 수정 버튼이 있어야함. 장소 수정 버튼을 누르면, 장소 수정 페이지로 이동.
    # 설명 아래에는 대표 이미지를 제외한 일반 이미지들이 표시되어야함. PLACE_IMAGE 중 PLACE_IMAGE.image_type이 sub인 이미지들을 표시.
    # 이미지는 멀티 캐로셀 형태로 여러 이미지들이 한번에 표시되는 형태로 구현. 이미지는 한번에 3개 ~ 5개 정도 표시. 모든 이미지를 표시하고, 좌우 화살표로 슬라이드 가능.
    # 이미지 아래에는 PLACE_ITEM들이 표시되어야함. PLACE_ITEM들은 카드 형태로 표시되어야함. 카드에는 상품 이미지, 상품 이름, 상품 설명, 상품 가격이 표시되어야함.
    # 상품 리스트는 아코디언 형태로, 접을 수 있어야함.
    # 상품 리스트에는 일정 확인 버튼이 있어야함. 일정 확인 버튼을 누르면, 캘린더에 각 상품별 일정이 표시되고, 캘린더 모달 창에는 결제 버튼이 있어야함.
    # 결제 버튼 클릭 시 purchase/request?item_id=상품ID로 이동하도록 구현.
    # 상품 리스트 아래에는 리뷰 리스트가 표시되어야함. 리뷰 리스트는 카드 형태로 표시되어야함. 카드에는 리뷰 작성자, 평점, 내용, 이미지, 작성일이 표시되어야함.
    # 리뷰 리스트 상단에는 리뷰를 작성할 수 있는 폼이 있어야함. 폼에는 평점, 내용, 이미지 업로드, 작성 버튼이 있어야함.
    # view에서 리뷰를 작성하지 않은 purchase가 있는지 확인, 없을 경우, 리뷰 작성 버튼의 onclick 이벤트를 비활성화. 리뷰 작성 가능한 상태일 경우, 리뷰 작성 버튼을 누르면, 리뷰가 작성되고, 리뷰 리스트가 갱신되어야함. purchase_id 필요.
    # 이미지 업로드는 필수가 아니며, 없을 경우 이미지가 표시되지 않아야함. 평점은 1 ~ 5까지 선택 가능하도록 구현.
    # 리뷰 아래에는 추천 장소 리스트가 표시되어야함. 추천 장소 리스트는 카드 형태로 표시되어야함. 카드에는 장소 이미지, 장소 이름, 장소 위치, 장소 소개가 표시되어야함.
    # 추천 리스트의 기준은 없음. 그냥 랜덤으로 6개의 장소를 가져와서 표시하면 됨. random을 사용해서 구현.
    path('detail', v.place_detail, name='place_detail'),

    # 장소 등록 페이지
    # 기본적으로 페이지가 로드되면 status가 writing인 장소가 하나 생성되도록 해야함. 이어쓰기까지는 불필요. 아래 일부 기능을 API나 별도의 섹션으로 구분하기 위함.
    # 1. 장소 정보 입력: 장소 이름, 짧은 소개, 장소 위치, 장소 위치 링크(구글 지도 링크), 장소 설명(html) 입력 폼이 있어야함.
    # 장소 설명 입력 폼은 Toastful Editor를 사용하여 구현.
    # 2. 장소 이미지 등록: 대표 이미지, 서브 이미지를 1개씩 등록하고, 등록된 이미지를 확인할 수 있도록 썸네일이 표시되어야함.
    # 이미지 썸네일 근처에는 이미지 삭제 버튼으로 다시 이미지를 삭제하고 등록할 수 있도록 구현.
    # 대표 이미지는 장소 카드 및 상단 캐로셀에 표시되며, 서브 이미지는 상세 정보에 작게 표시된다는 설명 택스트가 있어야함.
    # 3. 장소 상품 등록: 상품 이미지, 상품 이름, 상품 설명, 상품 가격을 입력할 수 있는 폼이 있어야함. 이미지는 필수. 여러 상품을 등록할 수 있어야함.
    # 4. 상품 일정 등록: 각 등록된 상품별로 일정을 등록할 수 있는 폼이 있어야함. 연도, 월, 일, 내용을 입력할 수 있어야함. 내용 입력은 자유롭게 택스트로 입력할 수 있어야함.
    # 5. 등록 버튼을 누르면, 장소가 등록되고, 등록된 장소 상세 페이지로 이동.
    # 모든 내용은 한번에 저장될 필요는 없음. 가능하면 각 내용마다 섹션을 두거나 또는 API를 이용해서 저장하는 방식으로 구현.(예: 장소 상품 등록이나 일정 등록은 별도의 API로 처리하는게 더 편할듯?)
    #path('write', v.place_write, name='place_write'),

    # 장소 수정 페이지
    # 원래 장소의 데이터를 불러와서 수정할 수 있는 폼이 있어야함. 수정할 수 있는 내용은 장소 정보, 장소 이미지, 장소 상품, 상품 일정이 있어야함.
    # 수정 버튼을 누르면, 장소가 수정되고, 수정된 장소 상세 페이지로 이동.
    # 이미지를 수정하거나, 상품, 상품 일정을 추가하거나 삭제할 수 있어야함.(연관 데이터를 수정할 수 있어야함)
    # 수정된 내용은 한번에 저장될 필요는 없음. 가능하면 각 내용마다 섹션을 두거나 또는 API를 이용해서 저장하는 방식으로 구현.
    # 수정된 내용을 저장하고 나서 장소 상세 페이지로 이동.
    path('edit', v.place_edit, name='place_edit'),

]