# Task 1 - Class Diagram: Food Delivery Platform

```mermaid
classDiagram
  class Customer {
    +int id
    +string name
    +string email
    +string phone
    +string deliveryAddress
    +placeOrder()
    +trackOrder(orderId)
    +writeReview(targetId, rating, comment)
  }
  class Restaurant {
    +int id
    +string name
    +string address
    +string openingHours
    +string status
    +updateMenu()
    +acceptOrder(orderId)
    +rejectOrder(orderId)
    +updateOrderStatus(orderId, status)
  }
  class MenuItem {
    +int id
    +string name
    +string description
    +float price
    +string category
    +bool available
  }
  class Order {
    +int id
    +date orderDate
    +string status
    +float totalPrice
    +calculateTotal()
    +cancel()
  }
  class OrderItem {
    +int id
    +int quantity
    +float unitPrice
  }
  class Courier {
    +int id
    +string name
    +string vehicleType
    +string location
    +string availability
    +acceptDelivery(orderId)
    +updateDeliveryStatus(orderId, status)
  }
  class Payment {
    +int id
    +float amount
    +string method
    +string status
    +process()
  }
  class Review {
    +int id
    +int rating
    +string comment
    +date date
  }

  Customer "1" --> "0..*" Order : places
  Order "1" --> "1" Restaurant : belongs to
  Order "1" --> "1..*" OrderItem : contains
  OrderItem "1" --> "1" MenuItem : refers to
  Restaurant "1" --> "0..*" MenuItem : offers
  Order "0..1" --> "1" Courier : assigned to
  Order "1" --> "1" Payment : has
  Customer "1" --> "0..*" Review : writes
  Review "0..*" --> "1" Restaurant : about
  Review "0..*" --> "1" Courier : about
```

## Design Justifications

- **Customer → Order (1 to 0..*)**: A customer may have zero orders (new account) or many over time.
- **Order → Restaurant (1 to 1)**: Each order is placed at exactly one restaurant — no mixed-restaurant orders.
- **Order → OrderItem (1 to 1..*)**: An order must contain at least one item.
- **Order → Courier (0..1 to 1)**: An order may not yet have a courier assigned (pending), but once assigned, exactly one courier delivers it.
- **Order → Payment (1 to 1)**: Every order requires exactly one payment record.
- **Restaurant/Courier ← Review (1 to 0..*)**: Reviews are optional feedback, so zero or many per target.
