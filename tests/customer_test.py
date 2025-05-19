import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee1 = Coffee("Espresso")
        self.coffee2 = Coffee("Latte")
    
    def test_init(self):
        self.assertEqual(self.customer.name, "Alice")
        self.assertEqual(len(self.customer.orders()), 0)
    
    def test_name_property(self):
        self.customer.name = "Bob"
        self.assertEqual(self.customer.name, "Bob")
        
        with self.assertRaises(TypeError):
            self.customer.name = 123
        
        with self.assertRaises(ValueError):
            self.customer.name = ""
        
        with self.assertRaises(ValueError):
            self.customer.name = "X" * 16
    
    def test_orders(self):
        self.assertEqual(len(self.customer.orders()), 0)
        
        order1 = self.customer.create_order(self.coffee1, 3.5)
        self.assertEqual(len(self.customer.orders()), 1)
        self.assertEqual(self.customer.orders()[0], order1)
        
        order2 = self.customer.create_order(self.coffee2, 4.5)
        self.assertEqual(len(self.customer.orders()), 2)
        self.assertEqual(self.customer.orders()[1], order2)
    
    def test_coffees(self):
        self.assertEqual(len(self.customer.coffees()), 0)
        
        self.customer.create_order(self.coffee1, 3.5)
        self.assertEqual(len(self.customer.coffees()), 1)
        self.assertEqual(self.customer.coffees()[0], self.coffee1)
        
        self.customer.create_order(self.coffee2, 4.5)
        self.assertEqual(len(self.customer.coffees()), 2)
        self.assertIn(self.coffee1, self.customer.coffees())
        self.assertIn(self.coffee2, self.customer.coffees())
        
        # Test duplicate coffee
        self.customer.create_order(self.coffee1, 3.0)
        self.assertEqual(len(self.customer.coffees()), 2)
    
    def test_create_order(self):
        order = self.customer.create_order(self.coffee1, 3.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee1)
        self.assertEqual(order.price, 3.5)
    
    def test_most_aficionado(self):
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Espresso")
        
        # No orders yet
        self.assertIsNone(Customer.most_aficionado(coffee))
        
        # One customer orders
        customer1.create_order(coffee, 3.5)
        self.assertEqual(Customer.most_aficionado(coffee), customer1)
        
        # Second customer orders more
        customer2.create_order(coffee, 4.0)
        customer2.create_order(coffee, 4.0)
        self.assertEqual(Customer.most_aficionado(coffee), customer2)
        
        # First customer catches up and surpasses
        customer1.create_order(coffee, 5.0)
        customer1.create_order(coffee, 4.0)
        self.assertEqual(Customer.most_aficionado(coffee), customer1)

if __name__ == "__main__":
    unittest.main()