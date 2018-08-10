from django.test import TestCase, Client
from django.contrib.auth.models import User
from financial_advisory import settings
from model_mommy import mommy

from investments.models import Equity, Index, IndexItem, Investment, Nature


class InvestmentTestCase(TestCase):

    def setUp(self):
        self.nature = mommy.make('investments.Nature')
        self.index = mommy.make('investments.Index')
        self.equity = mommy.make('investments.Equity')
        self.index_item = mommy.make('investments.IndexItem', index=self.index)
        self.investment = mommy.make(
            'investments.Investment', nature=self.nature, index=self.index
        )

    def test_create_nature(self):
        self.assertEquals(Nature.objects.count(), 1)

    def test_create_equity(self):
        self.assertEquals(Equity.objects.count(), 1)

    def test_create_index(self):
        self.assertEquals(Index.objects.count(), 1)

    def test_create_index_item(self):
        self.assertEquals(IndexItem.objects.count(), 1)

    def test_create_investment(self):
        self.assertEquals(Investment.objects.count(), 1)


class PagesTestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = mommy.prepare(User, username='guilherme')
        self.user.set_password('password')
        self.user.save()
        self.client.login(username='guilherme', password='password')

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/base.html')
        self.assertTemplateUsed(response, 'core/index.html')

    def test_investments_page(self):
        response = self.client.get('/investments/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/base.html')
        self.assertTemplateUsed(response, 'core/investments.html')
