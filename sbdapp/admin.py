from django.contrib import admin
from .models import GalleryImage, Testimonial

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'uploaded_at','image')
    search_fields = ('title',)
    list_filter = ('category', 'uploaded_at')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'review', 'created_at')
    search_fields = ('name', 'review')
    list_filter = ('created_at',)