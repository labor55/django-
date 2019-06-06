from django.contrib import admin
from login.models import Account
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name','user','pwd','created_time','modified_time']
    ordering = ['id']