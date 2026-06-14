# Task 0 - Problem Analysis: Food Delivery Platform

## 1. Main Entities

- Customer: A user who browses restaurants, places orders, and tracks deliveries. Attributes: name, email, phone, delivery address, payment method.
- Restaurant: A business that offers food items for order. Attributes: name, address, opening hours, status.
- MenuItem: A food item offered by a restaurant. Attributes: name, description, price, category, availability.
- Order: A request placed by a customer for one or more menu items. Attributes: order date, status, total price.
- OrderItem: A line item within an order, linking a menu item to a quantity. Attributes: quantity, unit price.
- Courier: A delivery person responsible for transporting orders. Attributes: name, vehicle type, current location, availability status.
- Payment: A transaction associated with an order. Attributes: amount, payment method, status.
- Review: Feedback left by a customer for a restaurant or courier. Attributes: rating, comment, date.

## 2. Key Relationships

- A Customer places one or more Orders.
- An Order belongs to exactly one Restaurant.
- An Order contains one or more OrderItems.
- An OrderItem references exactly one MenuItem.
- A Restaurant offers many MenuItems.
- An Order is assigned to one Courier.
- An Order has exactly one Payment.
- A Customer can write multiple Reviews.

## 3. Main Use Cases

### Customer
- Browse restaurants and menus
- Place an order
- Make a payment
- Track order status
- Cancel an order
- Rate and review a restaurant or courier

### Restaurant
- Manage menu
- Accept or reject orders
- Update order status

### Courier
- View available delivery requests
- Accept a delivery assignment
- Update delivery status

### System
- Calculate delivery time and fee
- Process payments
- Send notifications
- Match couriers to orders

## 4. Assumptions

- A Courier can only carry one active order at a time.
- Payment is processed when the order is placed.
- A Restaurant has a single menu.
- Reviews are tied to a completed Order.
