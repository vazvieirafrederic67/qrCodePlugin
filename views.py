from .models import QrCodeUrlPost
from django.views.generic import DetailView
from django.shortcuts import redirect

class QrCodePost(DetailView):
    model = QrCodeUrlPost
    url = model.url
    context_object_name = "post"
