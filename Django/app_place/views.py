from django.shortcuts import render, redirect
from app_core import daos as do
from app_core import models as mo

# 장소 정보 상세 페이지
def place_detail(request):

    # place id 확인
    place_id = request.GET.get("place_id")
    place = do.get_place_detail(place_id)
    if not place: # 장소 정보가 없을 경우
        return redirect('/')

    # 사용자가 구매한적이 있는지 확인
    reviewable = False
    for item in place['items']:
        try:
            if mo.PURCHASE.objects.select_related('item').filter(account=request.user, item__id=item['id']).exists():
                reviewable = True
                break
        except:
            pass

    contexts = {
        "place": place,
        'reviewable': reviewable
    }

    return render(request, 'place/detail.html', contexts)

# 장소 수정 페이지
def place_edit(request):
    place_id = request.GET.get("place_id")

    if not place_id:
        # place_id가 없으면 새로운 장소 생성
        new_place = do.create_place()
        if new_place["success"]:
            place_id = new_place["place_id"]

    place = do.get_place_detail(place_id)
    if not place: # 장소 정보가 없을 경우
        return redirect('/')

    return render(request, 'place/edit.html', {"place": place})
