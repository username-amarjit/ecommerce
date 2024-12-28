# Simple E-commerce API - Task List (Django REST Framework)

## Project Overview

In this project, you will build an e-commerce API using Django and Django REST Framework. Key features include JWT-based user authentication, product management, shopping cart handling, and payment gateway integration (Stripe/PayPal). The API will also require user and order management, along with appropriate error handling and security measures.

---

## Tasks

### 1. **Setup & Initial Configuration**
- [ ] **Initialize a new Django project**:
  - `django-admin startproject ecommerce_api`
  - Create a new app (e.g., `core` for common models or `shop` for product-related models): 
    - `python manage.py startapp shop`
- [ ] **Install dependencies**:
  - Django REST Framework: `pip install djangorestframework`
  - JWT Authentication: `pip install djangorestframework-simplejwt`
  - Stripe SDK for Python: `pip install stripe` (for payment integration)
  - Other utilities: `pip install djangorestframework-csv` (optional for CSV import/export)
- [ ] **Configure environment variables** (e.g., JWT secret, Stripe keys) using `django-environ` or `python-dotenv`.
- [ ] **Set up the database** (PostgreSQL, MySQL, or SQLite for local development).
> All Done
---

### 2. **User Authentication**
- [ ] **Create the User model** (extend `AbstractBaseUser` if custom fields are needed):
  - Fields: `email`, `password`, `role` (e.g., admin, customer), `is_active`, etc.
- [ ] **Create the User serializer**:
  - Use DRF's `UserSerializer` to handle user registration and login.
- [ ] **User Registration View**:
  - Endpoint to register a new user (`POST /api/auth/register`).
  - Hash the password using Django’s built-in `make_random_password` or `bcrypt`.
  - Return a success message and/or the created user.
- [ ] **User Login View**:
  - Endpoint to log in a user (`POST /api/auth/login`).
  - Authenticate using `email` and `password`, return a JWT token on success.
- [ ] **JWT Authentication**:
  - Set up JWT authentication using `SimpleJWT`.
  - Add `JWTAuthentication` in the `DEFAULT_AUTHENTICATION_CLASSES` in settings.
  - Protect certain endpoints (e.g., product creation, order creation) by requiring JWT.
- [ ] **JWT Refresh Token**:
  - Implement JWT refresh logic (`POST /api/auth/token/refresh`).

---

### 3. **Product Management**
- [ ] **Product Model**:
  - Define fields: `name`, `description`, `price`, `image_url`, `category`, `stock_quantity`, etc.
- [ ] **Create Product Serializer**:
  - Use DRF `ModelSerializer` for the `Product` model.
- [ ] **Product Listing View**:
  - Endpoint (`GET /api/products/`) to list all products with pagination and filtering (e.g., by category, price).
  - Optionally, implement ordering (e.g., by price or name).
> Done . filter is pending
- [ ] **Create Product View** (Admin only):
  - Endpoint (`POST /api/products/`) for admins to create products.
  - Ensure validation for fields like `price`, `name`, `stock_quantity`.
> 
- [ ] **Update Product View** (Admin only):
  - Endpoint (`PUT /api/products/{id}/`) for admins to update a product.
  - Validate inputs and update product details.
- [ ] **Delete Product View** (Admin only):
  - Endpoint (`DELETE /api/products/{id}/`) for admins to delete products.
  - Soft-delete or hard-delete (based on your preference).

---

### 4. **Shopping Cart Management**
- [ ] **Cart Model**:
  - Define a `CartItem` model with fields like `product`, `quantity`, `user`, and `total_price`.
- [ ] **Cart Serializer**:
  - Serialize the `CartItem` model to handle adding/removing products from the cart.
- [ ] **Add to Cart View**:
  - Endpoint (`POST /api/cart/`) to add products to the user's cart.
  - Validate stock and ensure cart item quantity is within available stock.
- [ ] **View Cart View**:
  - Endpoint (`GET /api/cart/`) to view the user's cart, including product details and total price.
- [ ] **Update Cart View**:
  - Endpoint (`PUT /api/cart/{id}/`) to update the quantity of a product in the cart.
- [ ] **Remove Item from Cart View**:
  - Endpoint (`DELETE /api/cart/{id}/`) to remove a specific product from the cart.

---

### 5. **Payment Gateway Integration (Stripe/PayPal)**
- [ ] **Configure Stripe/PayPal API keys**:
  - Store API keys in Django environment variables.
  - For Stripe: Set up the `stripe.api_key`.
- [ ] **Create Payment View**:
  - Endpoint (`POST /api/payment/`) to initiate payment.
  - Accept order details (e.g., products, total amount) and create a Stripe payment intent (or equivalent in PayPal).
  - Send payment data to Stripe/PayPal for processing.
- [ ] **Handle Payment Success**:
  - Set up webhook endpoints to listen for successful payments (`POST /api/payment/webhook/`).
  - Update order status to `paid` and generate the invoice.
- [ ] **Handle Payment Failure**:
  - Handle failure responses from the payment gateway and inform the user appropriately.

---

### 6. **Order Management**
- [ ] **Order Model**:
  - Define fields for order details: `user`, `products`, `total_price`, `payment_status`, `shipping_address`, `created_at`, etc.
  - Add a `ForeignKey` to `User` and `ManyToManyField` for products.
- [ ] **Create Order View**:
  - Endpoint (`POST /api/orders/`) to create an order after successful payment.
  - Deduct purchased items from stock and mark the order as `pending`.
- [ ] **View Orders (User)**:
  - Endpoint (`GET /api/orders/`) to view a user's past orders.
- [ ] **Admin Order Management**:
  - Endpoint (`GET /api/admin/orders/`) for admins to view all orders.
  - Admins can update order status (e.g., shipped, completed).
- [ ] **Order Tracking**:
  - Optionally, implement a tracking system (e.g., via a third-party service or custom logic).

---

### 7. **Product Inventory Management**
- [ ] **Update Stock on Order**:
  - When an order is created, reduce stock levels for the purchased products.
  - Ensure no order can be created if stock levels are insufficient.
- [ ] **Stock Alert** (Optional):
  - Implement an alert system for admins when stock for a product is low (e.g., below a threshold).

---

### 8. **Additional Features (Optional)**
- [ ] **Discounts and Coupons**:
  - Implement a `Coupon` model for applying discounts.
  - Add logic to apply coupons to the cart or during checkout.
- [ ] **Product Reviews and Ratings**:
  - Allow users to leave reviews for products (`POST /api/products/{id}/reviews/`).
  - Include fields like `rating`, `comment`, and `user`.
- [ ] **Wishlist**:
  - Implement a `Wishlist` model for users to save products they intend to buy later.

---

### 9. **Testing & Documentation**
- [ ] **Unit Tests**:
  - Write unit tests for critical functionality (authentication, product management, cart handling).
  - Use Django's `TestCase` and DRF's `APITestCase` for testing views.
- [ ] **API Documentation**:
  - Use tools like **Swagger** (via `drf-yasg` or `drf-spectacular`) to document API endpoints and their usage.
  - Include sample requests and responses.
  
---

### 10. **Deployment**
- [ ] **Deploy to a cloud provider**:
  - Use services like **Heroku**, **AWS**, **DigitalOcean**, or **Render** for deployment.
- [ ] **CI/CD**:
  - Set up continuous integration with GitHub Actions or CircleCI to automate deployment.

---

### 11. **Post-Deployment Monitoring**
- [ ] **Error Logging & Monitoring**:
  - Integrate error logging with **Sentry** or **Rollbar** to capture and notify of production errors.
- [ ] **Performance Monitoring**:
  - Use tools like **New Relic**, **Datadog**, or **AWS CloudWatch** to monitor API performance and response times.

---

## Final Notes

This project will require detailed attention to database models, user authentication, and payment gateway integration. Make sure to test thoroughly, especially around security (passwords, JWT, payment details) and data validation.