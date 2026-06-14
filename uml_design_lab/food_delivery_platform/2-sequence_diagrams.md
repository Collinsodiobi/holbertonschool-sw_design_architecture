# Task 2 - Sequence Diagrams: Food Delivery Platform

## 1. Place an order (mandatory use case)

```mermaid
sequenceDiagram
  participant C as Customer
  participant O as Order
  participant R as Restaurant
  participant P as Payment
  participant Sys as System

  C->>O: placeOrder()
  O->>R: acceptOrder(orderId)
  R-->>O: order accepted
  O->>O: calculateTotal()
  O->>P: process()
  P-->>O: payment status
  O-->>C: order confirmation
  O->>Sys: matchCourier(orderId)
  Sys-->>O: courier assigned
```

## 2. Courier delivers an order

```mermaid
sequenceDiagram
  participant Sys as System
  participant Co as Courier
  participant R as Restaurant
  participant O as Order
  participant C as Customer

  Sys->>Co: notify available delivery
  Co->>O: acceptDelivery(orderId)
  O-->>Co: assignment confirmed
  Co->>R: arrive at restaurant
  R-->>Co: hand over order
  Co->>O: updateDeliveryStatus(orderId, "picked up")
  O-->>C: order picked up
  Co->>O: updateDeliveryStatus(orderId, "delivered")
  O-->>C: order delivered
```

## 3. Customer writes a review

```mermaid
sequenceDiagram
  participant C as Customer
  participant Or as Order
  participant Rv as Review
  participant R as Restaurant
  participant Co as Courier

  C->>Or: check order status
  Or-->>C: status = "delivered"
  C->>Rv: writeReview(targetId, rating, comment)
  Rv->>R: attach review to restaurant
  Rv->>Co: attach review to courier
  Rv-->>C: review submitted
```

## Design Notes

- **Place an order** is the mandatory flow: customer triggers payment processing and courier matching happens automatically after confirmation.
- **Courier delivery** shows the courier as an active participant updating order status, which the customer observes via the Order object (consistent with Order being the central state-holder in the class diagram).
- **Review** can only be submitted after order status is "delivered", enforcing the assumption from Task 0 that reviews are tied to completed orders.
