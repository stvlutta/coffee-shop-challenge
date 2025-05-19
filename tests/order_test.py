import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")
        self.order = Order(self.customer, self.coffee, 3.5)
    
    def test_init(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.coffee, self.coffee)
        self.assertEqual(self.order.price, 3.5)
        
        # Test order added to coffee's orders
        self.assertIn(self.order, self.coffee.orders())
        
        # Test customer type validation
        with self.assertRaises(TypeError):
            Order("not a customer", self.coffee, 3.5)
        
        # Test coffee type validation
        with self.assertRaises(TypeError):
            Order(self.customer, "not a coffee", 3.5)
        
        # Test price validation
        with self.assertRaises(TypeError):
            Order(self.customer, self.coffee, "not a number")
        
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)  # too low
        
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)  # too high
    
    def test_customer_property(self):
        self.assertEqual(self.order.customer, self.customer)
        # Customer should be immutable
        self.assertFalse(hasattr(self.order.__class__, 'customer.setter'))
    
    def test_coffee_property(self):
        self.assertEqual(self.order.coffee, self.coffee)
        # Coffee should be immutable
        self.assertFalse(hasattr(self.order.__class__, 'coffee.setter'))
    
    def test_price_property(self):
        self.assertEqual(self.order.price, 3.5)
        # Price should be immutable after initialization
        self.assertFalse(hasattr(self.order.__class__, 'price.setter'))

if __name__ == "__main__":
    unittest.main()