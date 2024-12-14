from django.contrib import admin
from django.utils import timezone

from .models import Coin


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "symbol",
        "last_price",
        "created_at",
        "updated_at",
        "deleted_at",
    )
    list_filter = ("deleted_at", "created_at", "updated_at")
    search_fields = ("name", "symbol")
    readonly_fields = ("created_at", "updated_at", "deleted_at")
    ordering = ("-created_at",)  # Ordering by creation date, newest first

    def get_queryset(self, request):
        return Coin.objects.all()

    def delete_model(self, request, obj):
        obj.delete()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

    actions = ["soft_delete_coins", "restore_coins"]

    @admin.action(description="Soft delete selected coins")
    def soft_delete_coins(self, request, queryset):
        queryset.update(deleted_at=timezone.now())

    @admin.action(description="Restore selected coins")
    def restore_coins(self, request, queryset):
        queryset.update(deleted_at=None)
