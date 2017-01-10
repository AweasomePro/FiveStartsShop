from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from zhongtong.views.price import PriceViewSet

simpler_router = SimpleRouter()

urlpatterns = [
    url(r'', PriceViewSet.as_view()),
]
urlpatterns += simpler_router.urls
