from django.shortcuts import render

from .models import Btc

# Create your views here.


def index(request):
    bitcoin = Btc.objects.all()
    context = {"bitcoin": bitcoin}
    return render(request, "app_crypto/index.html", context)
