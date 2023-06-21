from django.urls import include, path
from rest_framework import routers

from ads.views import AdViewSet, CommentViewSet

# TODO настройка роутов для модели
ad_router = routers.SimpleRouter()
ad_router.register('ads', AdViewSet)
comment_router = routers.SimpleRouter()
comment_router.register('comments', CommentViewSet)

ads_urlpatterns = [
    path('api/', include(ad_router.urls)),
    path('api/', include(comment_router.urls)),
]
