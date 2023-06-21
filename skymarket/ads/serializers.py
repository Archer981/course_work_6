from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from ads.models import Ad, Comment
from users.models import User


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='full_name', many=False, read_only=True)

    # TODO сериалайзер для модели
    class Meta:
        model = Comment
        fields = '__all__'


# class AdUserSerializer(serializers.ModelSerializer):
#     author = SerializerMethodField()
#
#     def get_author(self, obj):
#         return f'{obj.first_name} {obj.last_name}'
#
#     class Meta:
#         model = User
#         fields = ['author']


class AdSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='full_name', many=False, read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    # author = AdUserSerializer()
    author = SlugRelatedField(slug_field='full_name', many=False, read_only=True)
    comments = SlugRelatedField(slug_field='text', many=True, read_only=True)
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ['id', 'author', 'title', 'price', 'description', 'created_at', 'image', 'comments']


class AdDetailSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='full_name', many=False, read_only=True)
    comments = SlugRelatedField(slug_field='text', many=True, read_only=True)

    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ['id', 'author', 'title', 'price', 'description', 'created_at', 'image', 'comments']
