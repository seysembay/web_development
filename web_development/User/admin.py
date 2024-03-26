from django.contrib import admin
from .models import CustomUser, Role
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    actions = ['reset_password']

    def reset_password(self, request, queryset):
        for user in queryset:
            user.set_password('new_password')  # Замените 'new_password' на новый пароль
            user.save()
        self.message_user(request, 'Password successfully reset for selected users.')

    reset_password.short_description = 'Reset password'


admin.site.register(CustomUser, CustomUserAdmin)


class User(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role')


# @admin.register(CustomUser)
# class User(admin.ModelAdmin):
#     list_display = ('username', 'first_name', 'last_name', 'role')


@admin.register(Role)
class User(admin.ModelAdmin):
    list_display = ('id', 'name')
