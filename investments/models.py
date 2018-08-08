from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    title = models.CharField(verbose_name='Nome', max_length=100)
    initial_amount = models.DecimalField(verbose_name='Aporte inicial', max_digits=10, decimal_places=2)
    nature = models.ForeignKey(
        'investments.Nature',
        verbose_name='Natureza',
        related_name='investments',
        on_delete=models.CASCADE,
    )
    index = models.ForeignKey(
        'investments.Index',
        verbose_name='Índice',
        related_name='investments',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    rate = models.DecimalField(
        verbose_name='Percentual',
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
    )
    tax = models.DecimalField(
        verbose_name='Tributação',
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
    )
    broker = models.CharField(
        verbose_name='Corretora',
        max_length=100,
        blank=True,
        null=True,
    )
    rent = models.DecimalField(
        verbose_name='Aluguel',
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
    )
    dividends = models.DecimalField(
        verbose_name='Dividendos',
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
    )
    date_initial_amount = models.DateTimeField(verbose_name='Data do aporte')
    due_date = models.DateTimeField(
        verbose_name='Data de vencimento',
        blank=True,
        null=True,
    )
    equity = models.ForeignKey(
        'investments.Equity',
        verbose_name='Patrimônio',
        related_name='investments',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    representativeness = models.DecimalField(
        verbose_name='Representatividade',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    @property
    def calculate_profitability(self):
        return Decimal(self.rate * (self.index.rate / 100)) or Decimal('0.0')

    @property
    def diff_month(self):
        initial = self.date_initial_amount
        now = timezone.now()
        return (now.year - initial.year) * 12 + now.month - initial.month

    @property
    def calculate_income(self):
        date = self.date_initial_amount
        day = date.day
        month = date.month
        year = date.year
        _, last_month_day = calendar.monthrange(year, month)
        profitability = 0
        first = True
        rate = self.rate
        value = self.initial_amount
        for i in range(self.diff_month):
            # TODO: Implement try and exception
            index_item = IndexItem.objects.get(
                index__title=self.index.title,
                period_from__year=year,
                period_from__month=month,
                period_until__year=year,
                period_until__month=month,
            )
            month += 1
            if month == 13:
                month = 1
                year += 1
            print('mês depois', month)
            print('ano depois', year)
            profitability += self.initial_amount * (index_item.rate / 100)
            print('rentabilidade', profitability)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Investimento'
        verbose_name_plural='Investimentos'


class Equity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Index(models.Model):
    title = models.CharField(verbose_name='Índice', max_length=30, db_index=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Índice'
        verbose_name_plural='Índices'


class IndexItem(models.Model):
    index = models.ForeignKey(Index, verbose_name='Índice', on_delete=models.CASCADE)
    rate = models.DecimalField(
        verbose_name='Percentual',
        max_digits=5,
        decimal_places=2,
    )
    period_from = models.DateTimeField(verbose_name='Período inicial', null=True, blank=True)
    period_until = models.DateTimeField(verbose_name='Período Final', null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.index.title

    class Meta:
        verbose_name='Índice Mensal'
        verbose_name_plural='Índices Mensais'
