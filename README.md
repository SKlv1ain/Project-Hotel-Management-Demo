
---

# Hotel Management System

A Django-based web application for managing hotel operations, including room management, bookings, payments, customer management, and reviews. This project provides a user-friendly interface for both customers and administrators, enabling seamless hotel management.

---

## Features

### **User Authentication**
- Secure login, signup, and logout functionality.
- Password hashing for enhanced security.

### **Room Management**
- Create, view, update, and delete rooms.
- Filter and sort rooms based on availability, type, and price.
- Calendar view to display room bookings.

### **Booking Management**
- Book rooms with real-time availability checks.
- Automatically calculates the total price based on room rates and duration.
- Bookings default to a `pending` status upon creation.
- Supports updating and canceling bookings.

### **Payment Management**
- Create and manage payments linked to bookings.
- Tracks payment status: `pending`, `confirmed`, or `failed`.
- Automatic price matching with associated bookings.

### **Customer Management**
- Manage customer profiles (create, edit, and delete).
- Store customer contact information securely.

### **Review System**
- Customers can leave ratings and comments on rooms they have booked.

---

## Technologies Used

- **Framework**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default), with support for PostgreSQL
- **Other Libraries**: Django Forms, Django Models, Django Signals

---

## Installation and Setup

### **Prerequisites**
- Python 3.8 or higher
- Virtualenv (recommended)
- Git

### **Steps to Set Up the Project**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/hotel-management-system.git
   cd hotel-management-system
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   - Run migrations to initialize the database schema:
     ```bash
     python manage.py migrate
     ```

5. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   - Open your browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Usage Instructions

### **For Administrators**
- Access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
- Use admin credentials to manage rooms, bookings, customers, and payments.

### **For Customers**
1. Sign up or log in to your account.
2. View available rooms and create a new booking.
3. Make payments and leave reviews for booked rooms.

---

## Folder Structure
```
PROJECT-HOTEL/
├── core/                   # Main application
│   ├── migrations/         # Django migrations
│   ├── static/             # Static files (CSS, JS, images)
│   ├── templates/          # HTML templates
│   ├── forms.py            # Form definitions
│   ├── models.py           # Database models
│   ├── views.py            # Application views
│   ├── admin.py            # Admin configuration
│   └── room_availability_check.js  # JavaScript for room availability
├── hotel_management/       # Project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # WSGI application
│   └── asgi.py             # ASGI application
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── .gitignore              # Git ignore file
```

---

## Key Features in Detail

### **Room Management**
- Rooms have attributes such as type, description, price, and status (`available`, `booked`, or `pending`).
- A calendar view shows room bookings for specific dates.

### **Booking Management**
- Supports filtering by price and availability.
- Automatically calculates the total price for a booking based on the duration and room rate.
- Bookings can be updated or canceled.

### **Payment Integration**
- Payments are linked to bookings.
- Payment statuses (`pending`, `confirmed`, or `failed`) are tracked and can trigger updates to booking statuses.

### **Customer Management**
- Manage customer data, including names, email, and phone numbers.
- View customer-related bookings and reviews.

### **Review System**
- Customers can leave ratings and comments for rooms they have booked.
- Reviews are displayed on room detail pages.

---

Here are some additional **SQL queries** that you can include in the **Features** section of your `README.md` to showcase how specific operations in your **Hotel Management System** can be accomplished using SQL. These queries reflect typical database interactions for features like room management, bookings, payments, and customer management.

---

## **Features with SQL Queries**

### **1. Room Management**

#### **Add a New Room**
```sql
INSERT INTO core_room (room_type, description, price_per_night, status, created_at, updated_at)
VALUES ('Deluxe', 'Spacious room with a king-size bed and a balcony', 150.00, 'available', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
```

#### **Get All Available Rooms**
```sql
SELECT * FROM core_room
WHERE status = 'available';
```

#### **Update Room Price**
```sql
UPDATE core_room
SET price_per_night = 200.00
WHERE id = 1; -- Replace 1 with the specific room ID
```

#### **Delete a Room**
```sql
DELETE FROM core_room
WHERE id = 5; -- Replace 5 with the specific room ID
```

---

### **2. Booking Management**

#### **Create a New Booking**
```sql
INSERT INTO core_booking (room_id, customer_id, check_in_date, check_out_date, total_price, status, created_at, updated_at)
VALUES (1, 2, '2024-12-01', '2024-12-05', 600.00, 'pending', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
```

#### **Get All Bookings for a Specific Room**
```sql
SELECT * FROM core_booking
WHERE room_id = 1;
```

#### **Get Confirmed Bookings Between Two Dates**
```sql
SELECT * FROM core_booking
WHERE status = 'confirmed'
  AND check_in_date >= '2024-12-01'
  AND check_out_date <= '2024-12-31';
```

#### **Cancel a Booking**
```sql
UPDATE core_booking
SET status = 'cancelled'
WHERE id = 3; -- Replace 3 with the specific booking ID
```

---

### **3. Payment Management**

#### **Record a New Payment**
```sql
INSERT INTO core_payment (booking_id, amount, status, created_at, updated_at)
VALUES (1, 600.00, 'pending', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
```

#### **Confirm a Payment**
```sql
UPDATE core_payment
SET status = 'confirmed'
WHERE id = 2; -- Replace 2 with the specific payment ID
```

#### **Get Total Payments for Confirmed Status**
```sql
SELECT SUM(amount) AS total_confirmed_payments
FROM core_payment
WHERE status = 'confirmed';
```

#### **View Payments for a Specific Booking**
```sql
SELECT * FROM core_payment
WHERE booking_id = 1;
```

---

### **4. Customer Management**

#### **Add a New Customer**
```sql
INSERT INTO core_customer (first_name, last_name, phone_num, email)
VALUES ('John', 'Doe', '123-456-7890', 'john.doe@example.com');
```

#### **Get All Customers Who Have Made Bookings**
```sql
SELECT DISTINCT c.*
FROM core_customer c
JOIN core_booking b ON c.id = b.customer_id;
```

#### **Update Customer Contact Information**
```sql
UPDATE core_customer
SET phone_num = '098-765-4321'
WHERE id = 2; -- Replace 2 with the specific customer ID
```

---

### **5. Review Management**

#### **Add a Review for a Room**
```sql
INSERT INTO core_review (customer_id, room_id, rating, comment, created_at)
VALUES (2, 1, 4.5, 'Great experience and very clean!', CURRENT_TIMESTAMP);
```

#### **Get Average Rating for a Room**
```sql
SELECT AVG(rating) AS average_rating
FROM core_review
WHERE room_id = 1; -- Replace 1 with the specific room ID
```

#### **Get All Reviews for a Specific Room**
```sql
SELECT r.*, c.first_name, c.last_name
FROM core_review r
JOIN core_customer c ON r.customer_id = c.id
WHERE room_id = 1;
```

---

### **6. Advanced Queries**

#### **Get Total Revenue from Bookings**
```sql
SELECT SUM(total_price) AS total_revenue
FROM core_booking
WHERE status = 'confirmed';
```

#### **List Rooms with the Most Bookings**
```sql
SELECT r.id AS room_id, r.room_type, COUNT(b.id) AS total_bookings
FROM core_room r
LEFT JOIN core_booking b ON r.id = b.room_id
GROUP BY r.id, r.room_type
ORDER BY total_bookings DESC;
```

#### **Get Active Bookings for a Customer**
```sql
SELECT b.*, r.room_type
FROM core_booking b
JOIN core_room r ON b.room_id = r.id
WHERE b.customer_id = 2
  AND b.status IN ('pending', 'confirmed');
```

---