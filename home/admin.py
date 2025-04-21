from django.contrib import admin
from .models import *

# Register your models here.
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at')
admin.site.register(UploadedImage, UploadedImageAdmin)


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'result', 'recommended_products')
admin.site.register(Diagnosis, DiagnosisAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(Product, ProductAdmin)


class SkinConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(SkinCondition, SkinConditionAdmin)