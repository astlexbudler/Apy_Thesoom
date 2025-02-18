from django.shortcuts import render
from app_core import daos as do
from app_core import models as mo

# 장소 정보 상세 페이지
def place_detail(request):
    return render(request, 'place/detail.html')

# 장소 등록 페이지
def place_write(request):
    return render(request, 'place/write.html')

# 장소 수정 페이지
def place_edit(request):
    place_id = request.GET.get("place_id")

    if not place_id:
        # place_id가 없으면 새로운 장소 생성
        new_place = do.create_place(
            name="",
            intro="",
            location="",
            location_link="",
            description="",
            status="writing"
        )

        if new_place["success"]:
            place_id = new_place["place_id"]
        else:
            return render(request, 'place/edit.html', {"error": new_place["message"]})

    try:
        place = mo.PLACE.objects.get(id=place_id)
    except mo.PLACE.DoesNotExist:
        return render(request, 'place/edit.html', {"error": "해당 장소를 찾을 수 없습니다."})

    return render(request, 'place/edit.html', {"place": place})
