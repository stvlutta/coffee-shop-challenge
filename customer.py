class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value
    
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list(set(order.coffee for order in self._orders))
    
    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order
    
    @classmethod
    def most_aficionado(cls, coffee):
        coffee_customers = [order.customer for order in coffee.orders()]
        if not coffee_customers:
            return None
        
        customer_spending = {}
        for order in coffee.orders():
            customer = order.customer
            if customer in customer_spending:
                customer_spending[customer] += order.price
            else:
                customer_spending[customer] = order.price
        
        return max(customer_spending.items(), key=lambda x: x[1])[0]