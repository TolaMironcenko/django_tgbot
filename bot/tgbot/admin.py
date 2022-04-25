from django.contrib import admin
from .models import UserInfo, Message


@admin.register(UserInfo, Message)
class MyAdmin(admin.ModelAdmin):
    pass

