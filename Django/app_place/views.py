from django.shortcuts import render

# 장소 정보 상세 페이지
def place_detail(request):
    return render(request, 'place/detail.html')

# 장소 등록 페이지
def place_write(request):
    return render(request, 'place/write.html')

# 장소 수정 페이지
def place_edit(request):
    return render(request, 'place/edit.html')