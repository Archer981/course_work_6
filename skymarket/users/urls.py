from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter


user_router = SimpleRouter()
user_router.register('users', UserViewSet, basename='users')

users_urlpatterns = [
    path('', include(user_router.urls))
]
