import unittest
from coffee import Coffee
from customer import Customer

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.coffee = Coffee("Espresso")
        self.customer1 = Customer("Alice")
        self.customer2 = Customer("Bob")
    
    def test_init(self):
        self.assertEqual(self.coffee.name, "Espresso")
        self.assertEqual(len(self.coffee.orders()), 0)
        
        with self.assertRaises(TypeError):
            Coffee(123)
        
        with self.assertRaises(ValueError):
            Coffee("Ab")  # too short
    
    def test_name_property(self):
        self.assertEqual(self.coffee.name, "Espresso")
        # Name should be immutable
        self.assertFalse(hasattr(self.coffee.__class__, 'name.setter'))
    
    def test_orders(self):
        self.assertEqual(len(self.coffee.orders()), 0)
        
        order1 = self.customer1.create_order(self.coffee, 3.5)
        self.assertEqual(len(self.coffee.orders()), 1)
        self.assertEqual(self.coffee.orders()[0], order1)
        
        order2 = self.customer2.create_order(self.coffee, 4.5)
        self.assertEqual(len(self.coffee.orders()), 2)
        self.assertEqual(self.coffee.orders()[1], order2)
    
    def test_customers(self):
        self.assertEqual(len(self.coffee.customers()), 0)
        
        self.customer1.create_order(self.coffee, 3.5)
        self.assertEqual(len(self.coffee.customers()), 1)
        self.assertEqual(self.coffee.customers()[0], self.customer1)
        
        self.customer2.create_order(self.coffee, 4.5)
        self.assertEqual(len(self.coffee.customers()), 2)
        self.assertIn(self.customer1, self.coffee.customers())
        self.assertIn(self.customer2, self.coffee.customers())
        
        # Test duplicate customer
        self.customer1.create_order(self.coffee, 3.0)
        self.assertEqual(len(self.coffee.customers()), 2)
    
    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 0)
        
        self.customer1.create_order(self.coffee, 3.5)
        self.assertEqual(self.coffee.num_orders(), 1)
        
        self.customer2.create_order(self.coffee, 4.5)
        self.assertEqual(self.coffee.num_orders(), 2)
    
    def test_average_price(self):
        self.assertEqual(self.coffee.average_price(), 0)
        
        self.customer1.create_order(self.coffee, 3.0)
        self.assertEqual(self.coffee.average_price(), 3.0)
        
        self.customer2.create_order(self.coffee, 5.0)
        self.assertEqual(self.coffee.average_price(), 4.0)
        
        self.customer1.create_order(self.coffee, 4.0)
        self.assertEqual(self.coffee.average_price(), 4.0)

if __name__ == "__main__":
    unittest.main()