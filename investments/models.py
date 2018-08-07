from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    title = models.CharField(verbose_name='Nome', max_length=100)
    nature = models.CharField(verbose_name='Natureza', max_length=100)
    initial_amount = models.DecimalField(verbose_name='Aporte inicial', max_digits=10, decimal_places=2)
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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Investimento'
        verbose_name_plural='Investimentos'


class Equity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Index(models.Model):
    title = models.CharField(verbose_name='Nome', max_length=50)
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
        return self.title

    class Meta:
        verbose_name='Índice'
        verbose_name_plural='Índices'
