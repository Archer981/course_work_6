from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ads.models import Ad, Comment
from users.models import User
# TODO Aдмика для пользователя - как реализовать ее можно подсмотреть в документаци django
# TODO Обычно её всегда оформляют, но в текущей задачи делать её не обязательно


# class AuthorAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(User, AuthorAdmin)

admin.site.register(User)
admin.site.register(Ad)
admin.site.register(Comment)
