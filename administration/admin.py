from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomUserAdmin(UserAdmin):
    ADDITIONAL_USER_FIELDS = (
        (
            None, {'fields': ('iban', 'created_by',)}
        ),
    )

    model = User
    form = MyUserChangeForm
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS


admin.site.register(User, CustomUserAdmin)
