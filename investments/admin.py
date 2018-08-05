from django.contrib import admin
from investments.models import Investment, Index


# Register your models here.
@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'nature', 'broker', 'due_date', 'representativeness', 'user',
    )
    list_filter = (
        'nature', 'broker', 'user',
    )
    search_fields = (
        'user', 'title', 'nature',
    )


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'rate', 'period_from', 'period_until',
    )
