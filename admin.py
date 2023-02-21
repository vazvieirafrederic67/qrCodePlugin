from django.contrib import admin

from .models import QrCodeUrlPost


class QrCodeUrlPostAdmin(admin.ModelAdmin):
    list_display = ("id", "img_preview", "slug", "link_preview", "name", "activate", "start_date", "created_at", "last_updated",)
    list_editable = ("activate",)
    readonly_fields = ["thumbnail"]
    fields = ['page_url', 'url', 'name', "start_date", "activate", ]


admin.site.register(QrCodeUrlPost, QrCodeUrlPostAdmin)
