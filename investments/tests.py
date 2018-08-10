from django.test import Client, TestCase
from model_mommy import mommy

from investments.models import Investment, Equity, Nature, Index, IndexItem


class InvestmentTestCase(TestCase):

    def setUp(self):
        self.investment = mommy.make('investments.Investment', _quantity=1)
        self.equity = mommy.make('investments.Equity')
        self.index_item = mommy.make('investments.IndexItem')

    def test_create_investment(self):
        self.assertEquals(Investment.objects.count(), 1)
        self.assertEquals(Equity.objects.count(), 1)
        self.assertEquals(Nature.objects.count(), 1)
        self.assertEquals(Index.objects.count(), 1)
        self.assertEquals(IndexItem.objects.count(), 1)
