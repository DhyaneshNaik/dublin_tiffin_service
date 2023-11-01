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
    def add_view(self, *args, **kwargs):
        self.inline = []
        return super(CustomUserAccountAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inline = [CustomUserAccountInLine]
        return super(CustomUserAccountAdmin, self).change_view(*args, **kwargs)

    inlines = (CustomUserAccountInLine,)



admin.site.unregister(User)
admin.site.register(User, CustomUserAccountAdmin)
admin.site.register(CustomUserAccountField)