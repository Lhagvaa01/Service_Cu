from django.contrib import admin
from django.utils.html import format_html

from .models import Users, InfoCUBranch, InfoProduct, History


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'TCUSERNAME', 'TCEMAIL', 'TCGENDER', 'isActive')
    search_fields = ('TCUSERNAME', 'TCEMAIL')
    list_filter = ('TCGENDER', 'isActive')


@admin.register(InfoCUBranch)
class InfoCUBranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'isActive', 'address', 'phone', 'createdDate')
    search_fields = ('name', 'address', 'id')
    list_filter = ('isActive', 'createdDate')


@admin.register(InfoProduct)
class InfoProductAdmin(admin.ModelAdmin):
    list_display = ('itemCode', 'itemName', 'itemPrice', 'isActive', 'createdDate', 'image_preview')
    search_fields = ('itemCode', 'itemName')

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="width: 50px; height: 50px;" />')
        return "-"
    image_preview.short_description = "Image Preview"


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'infoCUBranch', 'totalPrice', 'isPay', 'createdDate')
    search_fields = ('description',)
    list_filter = ('isPay', 'createdDate')
    filter_horizontal = ('infoProducts',)  # Many-to-Many талбарыг тохируулах
