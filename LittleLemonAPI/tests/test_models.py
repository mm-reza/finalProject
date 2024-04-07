from django.test import TestCase
from restaurant.models import MenuItem

class MenuTest(TestCase):
    def add_menu_test(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)