from django.contrib import admin


class CustomApplicationAdmin(admin.ModelAdmin):
    list_display = ("id",)


class CustomAccessTokenAdmin(admin.ModelAdmin):
    list_display = ("id",)


class CustomGrantAdmin(admin.ModelAdmin):
    list_display = ("id",)


class CustomRefreshTokenAdmin(admin.ModelAdmin):
    list_display = ("id",)


__all__ = [
    'CustomApplicationAdmin',
    'CustomAccessTokenAdmin',
    'CustomGrantAdmin',
    'CustomRefreshTokenAdmin',
]
