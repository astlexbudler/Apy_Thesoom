

from django.urls import path
from . import views as v


urlpatterns = [

    # 장소 정보 상세 페이지
    path('detail', v.place_detail, name='place_detail'),

    # 장소 등록 페이지
    path('write', v.place_write, name='place_write'),

    # 장소 수정 페이지
    path('edit', v.place_edit, name='place_edit'),

]