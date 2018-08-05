from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    title = models.CharField(verbose_name='Nome', max_length=100)
    nature = models.CharField(verbose_name='Natureza', max_length=100)
    initial_amount = models.DecimalField(verbose_name='Aporte inicial', max_digits=10, decimal_places=2)
    profitability = models.ForeignKey(
        'investments.Profitable',
        verbose_name='Rentabilidade',
        related_name='investments',
        on_delete=models.CASCADE,
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


class Profitable(models.Model):
    title = models.CharField(verbose_name='Nome', max_length=100)
    ipca = models.DecimalField(verbose_name='IPCA', max_digits=5, decimal_places=2, null=True, blank=True)
    cdi = models.DecimalField(verbose_name='CDI', max_digits=5, decimal_places=2, null=True, blank=True)
    selic = models.DecimalField(verbose_name='SELIC', max_digits=5, decimal_places=2, null=True, blank=True)
    flat_rate = models.DecimalField(verbose_name='Taxa fixa', max_digits=5, decimal_places=2, null=True, blank=True)
    period_from = models.DateTimeField(verbose_name='Período inicial', null=True, blank=True)
    period_until = models.DateTimeField(verbose_name='Período Final', null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)


class Equity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
