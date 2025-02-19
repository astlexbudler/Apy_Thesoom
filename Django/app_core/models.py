from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models

class ACCOUNT(AbstractUser):
    phone_validator = RegexValidator(
        regex=r'^\d+$',
        message="연락처는 숫자만 입력 가능합니다.",
    )
    phone_minimum_length_validator = MinLengthValidator(
        limit_value=7,
        message="연락처는 최소 7자리 이상이어야 합니다."
    )

    # id = models.AutoField(primary_key=True)
    # username = models.CharField(max_length=150, unique=True) 이메일
    # password = models.CharField(max_length=128)
    # first_name = models.CharField(max_length=30) # 이름
    # last_name = models.CharField(max_length=150) # 사용 안함
    # email = models.EmailField(max_length=254) # 사용 안함
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(auto_now_add=True)
    # last_login = models.DateTimeField(auto_now=True)
    # groups = models.ManyToManyField(Group)
    contact = models.CharField(max_length=20, validators=[phone_validator, phone_minimum_length_validator]) # 연락처
    account_type = models.CharField(max_length=50, verbose_name="사용 안함")

class PLACE(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="장소 이름")
    intro = models.CharField(max_length=500, verbose_name="짧은 소개")
    location = models.CharField(max_length=255, verbose_name="장소")
    location_link = models.CharField(max_length=300, verbose_name="장소")
    description = models.TextField(verbose_name="소개(html)")
    status = models.CharField(max_length=50, verbose_name="상태")
    discount_from_price = models.PositiveIntegerField(verbose_name="할인 전 가격")
    final_from_price = models.PositiveIntegerField(verbose_name="할인 후 가격")

class PLACE_IMAGE(models.Model):
    place = models.ForeignKey(PLACE, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="place_images/")
    image_type = models.CharField(max_length=50, verbose_name="이미지 타입, main, sub")
    order = models.PositiveIntegerField(verbose_name="이미지 표시 순서", default=0)

class PLACE_ITEM(models.Model):
    place = models.ForeignKey(PLACE, on_delete=models.CASCADE, related_name="items")
    image = models.ImageField(upload_to="place_items/", blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="상품 이름")
    description = models.TextField(verbose_name="설명(html)")
    price = models.PositiveIntegerField(verbose_name="가격")

class ITEM_DATE(models.Model):
    item = models.ForeignKey(PLACE_ITEM, on_delete=models.CASCADE, related_name="items")
    year = models.PositiveIntegerField(verbose_name="연도")
    month = models.PositiveIntegerField(verbose_name="월")
    date = models.PositiveIntegerField(verbose_name="날짜")
    content = models.TextField(verbose_name="표시할 내용")

class REVIEW(models.Model):
    place = models.ForeignKey(PLACE, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(ACCOUNT, on_delete=models.CASCADE, related_name="reviews")
    rate = models.PositiveIntegerField(verbose_name="평점")
    content = models.TextField(verbose_name="내용")
    images = models.FileField(upload_to="review_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

class PURCHASE(models.Model):
    account = models.ForeignKey(ACCOUNT, on_delete=models.CASCADE, related_name="purchases")
    item = models.ForeignKey(PLACE_ITEM, on_delete=models.CASCADE, related_name="purchases")
    book_start_datetime = models.DateTimeField(verbose_name="예약 시작 일시")
    book_end_datetime = models.DateTimeField(verbose_name="예약 종료 일시")
    memo = models.TextField(verbose_name="요청 사항")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="결제 시작 일시")
    purchase_at = models.DateTimeField(blank=True, null=True, verbose_name="결제 완료 일시")
    payment_agency = models.CharField(max_length=255, verbose_name="결제사")
    payment_method = models.CharField(max_length=255, verbose_name="결제 방법")
    payment_info = models.JSONField(verbose_name="결제 정보(json)")
    status = models.CharField(max_length=50, verbose_name="결제 상태")