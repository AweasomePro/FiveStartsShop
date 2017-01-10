from django.conf.urls import url, include
from . import price

urlpatterns = [
    url(r'^priceAndHourInterface/', include(price)),
]
