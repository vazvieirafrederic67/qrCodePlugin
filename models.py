import qrcode
from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe
from cms.models import Title
from django.contrib.sites.models import Site
import uuid


class QrCodeUrlPost(models.Model):
    TITLE_URLS = [(o.path, o.title) for o in Title.objects.filter(publisher_is_draft=False).exclude(path='')]

    uuid_field = models.UUIDField(blank=True, editable=False)
    page_url = models.CharField(blank=True, max_length=20, choices=TITLE_URLS)
    url = models.CharField(blank=True, max_length=255, verbose_name="Url")
    thumbnail = models.ImageField(blank=True, upload_to='qrCode')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=255, unique=True, verbose_name="Name")
    last_updated = models.DateTimeField(auto_now=True)
    start_date = models.DateField(blank=True, null=True)
    activate = models.BooleanField(default=False, verbose_name="Activate")
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        current_site = Site.objects.get_current()

        if not self.uuid_field:
            self.uuid_field = uuid.uuid4()

        self.slug = self.uuid_field

        if self.page_url:
            self.url = str(current_site.domain) + '/' + str(self.page_url)
            # self.url = 'http://127.0.0.1:8000/' + str(self.page_url)

        img = qrcode.make(self.url)
        type(img)  # qrcode.image.pil.PilImage
        img_name = str(self.slug) + '.png'
        img.save('./media/qrCode/' + img_name)

        self.thumbnail = img_name

        super().save(*args, **kwargs)

    def img_preview(self):
        return mark_safe(f'<img src = "/media/qrCode/{self.thumbnail}" width = "150"/>')

    def link_preview(self):
        return mark_safe(f'<a href="{self.url}" target=_blank>{self.uuid_field}</a>')
