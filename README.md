# 💰 Finance Tracking System (Python Backend)

## 📌 Overview

This project is a **Python-based finance tracking backend system** designed to manage financial transactions, generate insights, and enforce role-based access control.

It demonstrates strong backend engineering principles including:

* Clean architecture and modular design
* RESTful API development using FastAPI
* Data validation and error handling
* Business logic implementation (financial summaries & analytics)
* Role-based access control

The system is designed to serve as a backend for a finance dashboard or personal finance management application.

---

## 🚀 Tech Stack

* **Framework:** FastAPI
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Server:** Uvicorn

---

## 📂 Project Structure

```
finance_backend/
│
├── app/
│   ├── main.py
│   ├── db.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── routes/
│   └── utils/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone <your-repo-link>
cd finance_backend
```

---

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate:

* Windows:

```
venv\Scripts\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Run the Application

```
uvicorn app.main:app --reload
```

---

### 5. Open API Documentation

```
http://127.0.0.1:8000/docs
```

This provides an interactive UI to test all APIs.

---

## 🔐 Role-Based Access

This system implements **role-based access control** using request headers.

| Role    | Permissions                   |
| ------- | ----------------------------- |
| Viewer  | View records & summaries      |
| Analyst | View + access analytics       |
| Admin   | Full access (CRUD operations) |

### Example Header:

```
role: admin
```

> Note: Authentication is simulated via headers for simplicity.

---

## 📊 Features

### ✅ 1. Financial Record Management

* Create transactions
* View transactions
* Update transactions
* Delete transactions
* Filter by:

  * Type (income/expense)
  * Category
  * Date range
* Pagination support

---

### ✅ 2. Summary & Analytics

* Total income
* Total expenses
* Current balance
* Category-wise breakdown
* Monthly summary
* Recent transactions

---

### ✅ 3. Validation & Error Handling

* Input validation using Pydantic
* Proper HTTP status codes
* Error handling for:

  * Invalid input
  * Unauthorized access
  * Missing resources

---

### ✅ 4. Database & Persistence

* SQLite database
* SQLAlchemy ORM
* Persistent storage across restarts

---

## 🔌 API Endpoints

### 🔹 Transactions

* `POST /transactions/` → Create transaction
* `GET /transactions/` → List transactions (with filters & pagination)
* `PUT /transactions/{id}` → Update transaction
* `DELETE /transactions/{id}` → Delete transaction

---

### 🔹 Summary

* `GET /summary/` → Overall summary
* `GET /summary/category` → Category breakdown
* `GET /summary/monthly` → Monthly summary
* `GET /summary/recent` → Recent transactions

---

## 🧪 Testing

The application can be tested using:

* FastAPI Swagger UI (`/docs`)
* cURL or Postman

### Sample Test Flow:

1. Create transactions
2. Fetch transactions
3. Apply filters
4. Update a transaction
5. View summary analytics
6. Test role-based restrictions

---

## ⚠️ Assumptions

* Authentication is simplified using headers
* SQLite is used for simplicity and portability
* Categories are free-text (no predefined list)
* Single-user environment (no multi-user ownership yet)

---

## 🚀 Future Improvements

* JWT-based authentication
* User-specific transaction ownership
* Advanced analytics (yearly trends, forecasting)
* Export to CSV/Excel
* Unit and integration tests
* Docker support for deployment

---

## 🧠 Design Highlights

* Clear separation of concerns:

  * Routes → API layer
  * Services → Business logic
  * Models → Database schema
* Scalable and maintainable architecture
* Clean and readable Python code

---

## 📌 Conclusion

This project demonstrates the ability to:

* Design and implement a backend system
* Handle real-world data and business logic
* Build scalable and maintainable Python applications

---

## 👤 Author

**Faizal Mistry**

---
