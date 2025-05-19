from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create some coffees
espresso = Coffee("Espresso")
latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino")

# Create orders
alice.create_order(espresso, 3.5)
alice.create_order(latte, 4.5)
bob.create_order(cappuccino, 5.0)
bob.create_order(espresso, 3.0)

# Debug output
print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
print(f"Bob's coffees: {[coffee.name for coffee in bob.coffees()]}")
print(f"Espresso customers: {[customer.name for customer in espresso.customers()]}")
print(f"Latte customers: {[customer.name for customer in latte.customers()]}")
print(f"Cappuccino customers: {[customer.name for customer in cappuccino.customers()]}")
print(f"Espresso orders: {espresso.num_orders()}")
print(f"Espresso average price: ${espresso.average_price():.2f}")
print(f"Most espresso aficionado: {Customer.most_aficionado(espresso).name if Customer.most_aficionado(espresso) else 'None'}")