# 🛒 E-commerce Product API

## 📌 Project Overview

The **E-commerce Product API** is a RESTful backend service built with **Django** and **Django REST Framework (DRF)** that allows users to manage products and user accounts for an e-commerce platform.
It provides full **CRUD functionality**, powerful **search and filtering**, and **JWT-based authentication** for secure access.

This API can be easily integrated with web and mobile front-end applications.

---

## ✨ Features

### 🔐 User Management

* Register new users
* Update user profiles
* Delete users
* View user information

### 📦 Product Management

* Add new products
* Update product details
* Delete products
* View product details

### 🔍 Search & Filtering

* Search products by name
* Filter products by:

  * Category
  * Price
  * Availability

### ⭐ Optional Features

* Product ratings and reviews
* Pagination for product listings
* JWT authentication for protected endpoints

---

## 🛠️ Technologies Used

* **Backend:** Django, Django REST Framework
* **Database:** SQLite (development), PostgreSQL (production)
* **Authentication:** JSON Web Tokens (JWT)
* **Testing:** Postman
* **Deployment:** Heroku or PythonAnywhere

---

## 📁 Project Structure

```
ecommerce_product_api/
│
├── ecommerce_api/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── products/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ecommerce-product-api.git
cd ecommerce-product-api
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file and add:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=db.sqlite3
```

---

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Start the Development Server

```bash
python manage.py runserver
```

---

## 🔑 Authentication

This project uses **JWT Authentication**.

### Obtain Token

```http
POST /api/token/
```

**Request Body:**

```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

### Use Token in Requests

Add this header:

```
Authorization: Bearer <your_access_token>
```

---

## 📡 API Endpoints

### 👤 User Endpoints

| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| POST   | `/api/users/`      | Register a new user |
| GET    | `/api/users/{id}/` | Get user details    |
| PUT    | `/api/users/{id}/` | Update user         |
| DELETE | `/api/users/{id}/` | Delete user         |
| POST   | `/api/token/`      | Get JWT token       |

---

### 📦 Product Endpoints

| Method | Endpoint                                      | Description              |
| ------ | --------------------------------------------- | ------------------------ |
| POST   | `/api/products/`                              | Create a product         |
| GET    | `/api/products/`                              | List all products        |
| GET    | `/api/products/{id}/`                         | Get single product       |
| PUT    | `/api/products/{id}/`                         | Update product           |
| DELETE | `/api/products/{id}/`                         | Delete product           |
| GET    | `/api/products/search/?name=xyz&category=abc` | Search & filter products |

---

## 🧪 Testing the API

Use **Postman** to test endpoints:

1. Register a user
2. Get a JWT token
3. Use the token to access protected routes

---

## 🗓️ Project Timeline

| Week   | Tasks                                          |
| ------ | ---------------------------------------------- |
| Week 1 | Setup Django project, DRF, user authentication |
| Week 2 | Product model & CRUD implementation            |
| Week 3 | Search, filtering, pagination                  |
| Week 4 | Unit testing & JWT security                    |
| Week 5 | Deployment & documentation                     |

---

## 🚀 Deployment

You can deploy this project on:

* **Heroku**
* **PythonAnywhere**

Steps:

1. Configure PostgreSQL
2. Update environment variables
3. Push code to hosting platform
