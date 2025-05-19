# Coffee Shop Challenge

A Python application that simulates a coffee shop system with customers, coffees, and order management.

## Overview

This project implements a simple object-oriented model of a coffee shop where:
- Customers can order various types of coffee
- Each coffee has a price and can be ordered multiple times
- The system tracks orders, customer preferences, and coffee popularity

## Classes

### Coffee
- Represents a type of coffee with a name
- Tracks all orders for this coffee type
- Provides statistics like average price and number of orders

### Customer
- Represents a coffee shop customer
- Can create orders for different coffees
- Keeps track of their order history
- Includes a class method to find the customer who spent the most on a specific coffee

### Order
- Represents a single purchase of a coffee by a customer
- Links a customer to a coffee with a specific price
- Maintains bidirectional relationships with both Customer and Coffee

## Requirements

- Python 3.8+
- No external dependencies required

## Installation

Clone this repository:

```bash
git clone <repository-url>
cd coffee-shop-challenge
```

## Usage

```python
from customer import Customer
from coffee import Coffee

# Create customers and coffees
alice = Customer("Alice")
bob = Customer("Bob")
espresso = Coffee("Espresso")
latte = Coffee("Latte")

# Create orders
alice.create_order(espresso, 3.5)
bob.create_order(latte, 4.5)

# Get customer's ordered coffees
alice_coffees = alice.coffees()  # Returns [espresso]

# Get coffee's customers
espresso_customers = espresso.customers()  # Returns [alice]

# Find the customer who spent the most on espresso
aficionado = Customer.most_aficionado(espresso)  # Returns alice
```

### Demo Script

Run the debug script to see the system in action:

```bash
python debug.py
```

## Testing

Run the test suite:

```bash
python -m unittest discover tests
```

## Project Structure

- `coffee.py` - Coffee class implementation
- `customer.py` - Customer class implementation
- `order.py` - Order class implementation 
- `debug.py` - Demo script with sample usage
- `tests/` - Test suite for all classes