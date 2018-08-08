from django.contrib import admin
from investments.models import Investment, Index, IndexItem, Nature


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


@admin.register(Nature)
class NatureAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('title', 'date_added', )
    search_fields = ('title', )


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('title', 'date_added', )
    search_fields = ('title', )


@admin.register(IndexItem)
class IndexItemAdmin(admin.ModelAdmin):
    list_display = (
        'index', 'rate', 'period_from', 'period_until',
    )
