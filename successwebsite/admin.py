from django.contrib import admin
from .models import Audio, Gallery, Shop, Tour

# Register your models here.
@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'release_date', 'audio')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('photo_title', 'image', 'date_added')

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('shop_items', 'products_name', 'products_price')

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('tour_name', 'date_added', 'venue')