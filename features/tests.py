from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from features.views import *
from features.models import *

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, customers)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = customers(request)
        self.assertTrue(response.content.startswith(b'<html lang="en">'))
        self.assertIn(b'<title>Customers</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

class CustomerDetailTest(TestCase):

    def test_customers_url_resolves_to_customer_detail_view(self):
        found = resolve('/customers/1/')
        self.assertEqual(found.func, customer_detail)

    def create_john(self, name="John", last_viewed_feature="2015-03-01 19:10:00"):
        return Customer.objects.create(name=name, last_viewed_feature=last_viewed_feature)

    def test_create_john(self):
        create = self.create_john()
        john = Customer.objects.get(pk=1)
        self.assertTrue(isinstance(create, Customer))
        self.assertEqual(john.name, "John")

class CustomerFeaturesTest(TestCase):

    def test_customers_features_url_resolves_to_new_features_view(self):
        found = resolve('/customers/1/new-features')
        self.assertEqual(found.func, new_features)