from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Ad
from ads.permissions import IsOwner, IsAdmin
from ads.serializers import *


# class AdPagination(pagination.PageNumberPagination):
#     pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializers = {
        'list': AdListSerializer,
        'retrieve': AdDetailSerializer,
        # 'create': AdCreateSerializer,
    }
    default_serializer = AdSerializer
    permissions = {
        'list': [AllowAny],
        'create': [IsAuthenticated],
        'retrieve': [IsOwner | IsAdmin],
        'update': [IsOwner | IsAdmin],
        'destroy': [IsOwner | IsAdmin],
        'partial_update': [IsOwner | IsAdmin],
    }
    default_permission = [AllowAny]

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permission)
        return super().get_permissions()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        title = request.GET.get('title')
        if title:
            self.queryset = self.queryset.filter(title__icontains=title)
        description = request.GET.get('description')
        if description:
            self.queryset = self.queryset.filter(description__icontains=description)
        return super().list(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.object.image = request.FILES.get('image')
        self.object.save()
        return JsonResponse(self.object.serialize(), safe=False)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    serializers = {
        # 'list': AdListSerializer,
        # 'retrieve': AdDetailSerializer,
        # 'create': AdCreateSerializer,
    }
    default_serializer = CommentSerializer

    permissions = {
        'list': [IsOwner | IsAdmin],
        'create': [IsAuthenticated],
        'retrieve': [IsOwner | IsAdmin],
        'update': [IsOwner | IsAdmin],
        'destroy': [IsOwner | IsAdmin],
        'partial_update': [IsOwner | IsAdmin],
    }
    default_permission = [AllowAny]

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permission)
        return super().get_permissions()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

