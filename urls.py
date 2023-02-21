from django.urls import path
from .views import QrCodePost


app_name = "qrCodePost"

urlpatterns = [
    path('qrCode/<str:slug>/', QrCodePost.as_view(), name='post'),
]