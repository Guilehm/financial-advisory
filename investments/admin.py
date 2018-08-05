from django.contrib import admin
from investments.models import Investment, Profitable


# Register your models here.
@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'title', 'nature', 'broker', 'due_date', 'representativeness'
    )
    list_filter = (
        'user', 'nature', 'broker',
    )
    search_fields = (
        'user', 'title', 'nature',
    )


@admin.register(Profitable)
class ProfitableAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'ipca', 'cdi', 'selic', 'flat_rate',
    )
