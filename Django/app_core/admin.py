from django.contrib import admin
from . import models

class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'is_staff', 'is_superuser', 'date_joined', 'last_login', 'contact']
    search_fields = ['username', 'first_name', 'contact']
    list_filter = ['is_staff', 'is_superuser', 'date_joined', 'last_login']

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'intro', 'location', 'status', 'discount_from_price', 'final_from_price']
    search_fields = ['name', 'location', 'status']
    list_filter = ['status']

class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'image', 'image_type', 'order']
    search_fields = ['place', 'image_type']
    list_filter = ['image_type']

class PlaceItemAdmin(admin.ModelAdmin):
    list_display = ['place', 'image', 'name', 'price']
    search_fields = ['place', 'name']
    list_filter = ['price']

class ItemDateAdmin(admin.ModelAdmin):
    list_display = ['item', 'year', 'month', 'date', 'content']
    search_fields = ['item', 'content']
    list_filter = ['year', 'month', 'date']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['place', 'author', 'rate', 'content', 'images', 'created_at']
    search_fields = ['place', 'author', 'content']
    list_filter = ['rate', 'created_at']

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['account', 'item', 'book_start_datetime', 'book_end_datetime', 'memo', 'created_at', 'purchase_at', 'payment_agency', 'payment_method', 'payment_info', 'status']
    search_fields = ['account', 'item', 'memo', 'payment_agency', 'payment_method', 'status']
    list_filter = ['book_start_datetime', 'book_end_datetime', 'created_at', 'purchase_at', 'status']

admin.site.register(models.ACCOUNT, AccountAdmin)
admin.site.register(models.PLACE, PlaceAdmin)
admin.site.register(models.PLACE_IMAGE, PlaceImageAdmin)
admin.site.register(models.PLACE_ITEM, PlaceItemAdmin)
admin.site.register(models.ITEM_DATE, ItemDateAdmin)
admin.site.register(models.REVIEW, ReviewAdmin)
admin.site.register(models.PURCHASE, PurchaseAdmin)
