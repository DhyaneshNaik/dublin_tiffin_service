from django.contrib import admin
from customuser.models import CustomUserAccountField
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# Add customuser fields to existing User fields
class CustomUserAccountInLine(admin.StackedInline):
    model = CustomUserAccountField
    can_delete = False
    verbose_name_plural = 'CustomUserAccountField'


class CustomUserAccountAdmin(UserAdmin):
    inlines = (CustomUserAccountInLine,)


admin.site.unregister(User)
admin.site.register(User, CustomUserAccountAdmin)
admin.site.register(CustomUserAccountField)