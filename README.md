```markdown
# 🛒 E-commerce Product API

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.2-green)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15-blueviolet)](https://www.django-rest-framework.org/)
[![Render](https://img.shields.io/badge/deploy-render-brightgreen)](https://render.com/)

---

## 📌 Project Overview

The **E-commerce Product API** is a RESTful backend service built with **Django** and **Django REST Framework (DRF)** that allows users to manage **products** and **user accounts** for an e-commerce platform.  

It provides:

- Full **CRUD functionality**
- **Search and filtering**
- **Basic authentication** for secure access  

This API is designed to be easily integrated with web or mobile frontend applications.

**Live Demo:** [🔗 Click here once deployed](https://your-render-app.onrender.com)

---

## ✨ Features

### 🔐 User Management

- Register new users
- Update user profiles
- Delete users
- View user information

### 📦 Product Management

- Add new products
- Update product details
- Delete products
- View product details

### 🔍 Search & Filtering

- Search products by name
- Filter products by:
  - Category
  - Price
  - Availability

### ⭐ Optional Features

- Product ratings and reviews
- Pagination for product listings
- Interactive API docs (Swagger / Redoc)

---

## 🛠️ Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** SQLite (development), PostgreSQL (production)
- **Authentication:** Basic Authentication
- **Testing:** Postman
- **Deployment:** Render
- **Documentation:** drf-yasg (Swagger / Redoc)

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
├── media/
│   └── product_images/
├── static/
├── manage.py
└── requirements.txt

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/meraman750/E-commerce.git
cd ecommerce-product-api
````

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
DATABASE_NAME=db.sqlite3   # For development
```

**Optional for Production (PostgreSQL on Render):**

```env
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```

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

This project uses **Basic Authentication**.

* Use your **username and password** to access protected endpoints.
* You can authenticate using Postman or any REST client by selecting **Basic Auth**.

---

## 📡 API Endpoints

### 👤 User Endpoints

| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| POST   | `/api/users/`      | Register a new user |
| GET    | `/api/users/{id}/` | Get user details    |
| PUT    | `/api/update/{id}/` | Update user         |
| DELETE | `/api/delete/{id}/` | Delete user         |

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
2. Authenticate using **Basic Auth**
3. Use your credentials to access protected routes

**Optional:** Import the Postman collection from `/docs/postman_collection.json`

---

## 🗓️ Project Timeline

| Week   | Tasks                                          |
| ------ | ---------------------------------------------- |
| Week 1 | Setup Django project, DRF, user authentication |
| Week 2 | Product model & CRUD implementation            |
| Week 3 | Search, filtering, pagination                  |
| Week 4 | Unit testing & security                        |
| Week 5 | Deployment & documentation                     |

---

## 🚀 Deployment

You can deploy this project on:

* **Render** (recommended)
* **Heroku**
* **PythonAnywhere**

**Deployment Steps on Render:**

1. Configure **PostgreSQL**
2. Add environment variables in Render dashboard
3. Push code to GitHub
4. Connect Render to GitHub repo
5. Set build & start commands:

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
gunicorn ecommerce_api.wsgi
```

6. Deploy → Live URL ready

---

## 📄 API Documentation

Interactive documentation available using **Swagger / Redoc** (via `drf-yasg`):

* Swagger UI: `/swagger/`
* Redoc UI: `/redoc/`


