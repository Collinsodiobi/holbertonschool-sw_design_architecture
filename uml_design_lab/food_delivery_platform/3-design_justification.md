# Task 3 - Design Justification: Food Delivery Platform

## 1. Main Design Decisions

- We modeled the system around **8 core classes**: Customer, Restaurant, MenuItem, Order, OrderItem, Courier, Payment, and Review.
- **Order** is the central entity of the system — it links Customer, Restaurant, OrderItems, Payment, and Courier together. This reflects the real-world flow: everything in a food delivery app revolves around an order's lifecycle.
- We separated **MenuItem** (what a restaurant offers) from **OrderItem** (what was actually ordered, with quantity and price at time of order). This avoids issues if a restaurant changes a menu price later — the order keeps the historical price.
- **Payment** is its own class rather than fields on Order, so payment logic (processing, retries, refunds) can evolve independently of order logic.

## 2. Distribution of Responsibilities

- **Customer**: initiates actions (placeOrder, trackOrder, writeReview) — represents the user-facing side.
- **Restaurant**: manages its own menu and decides to accept/reject orders — keeps menu management logic local to the restaurant.
- **Order**: owns the order lifecycle (calculateTotal, cancel) and coordinates with Payment and Courier — acts as the "orchestrator" of a transaction.
- **Courier**: manages delivery-specific actions (acceptDelivery, updateDeliveryStatus) — keeps delivery logic separate from order logic, since a courier could theoretically be reassigned.
- **Payment**: isolated processing logic (process()) — single responsibility for handling transactions.
- **Review**: standalone feedback object tied to a completed order, but referencing Restaurant or Courier as its target.

This follows the **Single Responsibility Principle** — each class has one clear reason to change.

## 3. Relationships and Multiplicities

- **Customer 1 -- 0..* Order**: a customer can exist with zero orders (new signup) or many over time.
- **Order 1 -- 1 Restaurant**: an order is tied to exactly one restaurant — we decided against supporting multi-restaurant orders to avoid unnecessary complexity (per the "avoid over-engineering" guideline).
- **Order 1 -- 1..* OrderItem**: an order must have at least one item — an empty order makes no sense.
- **Restaurant 1 -- 0..* MenuItem**: a restaurant can have zero items initially (newly onboarded) or many.
- **Order 0..1 -- 1 Courier**: an order may have no courier yet (pending/being prepared), but once assigned, exactly one courier delivers it. We chose 0..1 rather than mandatory 1 to reflect the real order lifecycle (orders aren't created with a courier already attached).
- **Order 1 -- 1 Payment**: every order requires exactly one payment record — simplifies tracking (no split payments in this design).
- **Customer 1 -- 0..* Review**, **Restaurant/Courier 1 -- 0..* Review**: reviews are optional and can accumulate over time.

## 4. Alternatives Considered

- **Single Menu table with restaurant_id vs. embedding menu in Restaurant**: We chose a separate MenuItem class linked by foreign key for normalization and to allow easy querying/filtering of items independent of the restaurant object.
- **Courier carrying multiple orders simultaneously**: We considered allowing a courier to be assigned to multiple active orders (batch deliveries), but simplified to one order per courier at a time for this design, since it reduces complexity in the sequence diagrams and matches a common "single delivery" mental model. This could be revisited if requirements demanded batching.
- **Payment embedded directly in Order vs. separate class**: Initially considered just adding `paymentStatus` and `amount` fields to Order. We decided a separate Payment class is more extensible (different payment methods, retry logic, refunds) without bloating the Order class.
- **Single review type vs. separate ReviewRestaurant/ReviewCourier classes**: We used one generic Review class with a target reference, rather than two separate classes, to avoid duplicating the rating/comment/date structure (DRY principle).

## 5. Trade-offs

- **Simplicity vs. flexibility**: Restricting orders to a single restaurant and a single courier per order simplifies the model significantly but would require redesign if the business wanted multi-restaurant carts or batch deliveries.
- **Normalization vs. query complexity**: Separating MenuItem and OrderItem adds a join/lookup step but protects historical order data from menu changes — we felt this was worth the trade-off.
- **Generic Review vs. type-specific reviews**: A single Review class is simpler to maintain but means validation logic (e.g., "a courier review must reference a delivered order") needs to be enforced at the application level rather than the schema level.

## 6. What Would Change If Requirements Changed

- If the platform needed **multi-restaurant orders** (e.g. a "cart" spanning several restaurants), we'd introduce a `Cart` class containing multiple `SubOrders`, each tied to one restaurant — Order would become a parent grouping of SubOrders.
- If **couriers needed to batch multiple deliveries**, the Order–Courier relationship would change from 0..1 -- 1 to 0..* -- 1, and the sequence diagram for delivery would need a queue/list of assigned orders.
- If **split payments** were required, Payment would move from 1--1 to 1--0..* relative to Order.
