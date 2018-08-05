from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    nature = models.CharField(max_length=100)
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)
    profitability = models.ForeignKey(
        'investments.Profitable',
        related_name='investments',
        on_delete=models.CASCADE,
    )
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    broker = models.CharField(max_length=100)
    rent = models.DecimalField(max_digits=8, decimal_places=2)
    dividends = models.DecimalField(max_digits=8, decimal_places=2)
    date_initial_amount = models.DateTimeField()
    due_date = models.DateTimeField()
    equity = models.ForeignKey(
        'investments.Equity',
        related_name='investments',
        on_delete=models.CASCADE,
    )
    representativeness = models.DecimalField(max_digits=10, decimal_places=2)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)


class Profitable(models.Model):
    title = models.CharField(max_length=100)
    ipca = models.DecimalField(max_digits=5, decimal_places=2)
    cdi = models.DecimalField(max_digits=5, decimal_places=2)
    selic = models.DecimalField(max_digits=5, decimal_places=2)
    flat_rate = models.DecimalField(max_digits=5, decimal_places=2)
    period_from = models.DateTimeField()
    period_until = models.DateTimeField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)


class Equity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
