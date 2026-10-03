# 0. AI: SQL to ORM Refactoring and Security Analysis

## 📌 Project Overview
This repository folder contains the solution for **AI Lab Assignment: SQL to ORM Refactoring and Security Analysis**. The goal of this assignment is to translate a procedural database script using raw MySQL query strings into a modern, robust, type-safe, and object-oriented solution using the **SQLAlchemy Object-Relational Mapper (ORM)**.

---

## 📂 Repository Contents
- **`procedural_user_manager.py`**: Initial procedural Python database module using `mysql-connector-python` and raw parameterized SQL queries.
- **`orm_user_manager.py`**: Modernized, object-oriented SQLAlchemy ORM implementation featuring a `User` declarative model, session management, schema creation, and object-centric CRUD operations.
- **`README.md`**: Technical documentation detailing prompt formulation, security analysis, abstraction benefits, and maintainability comparisons.

---

## 🤖 AI Prompt Formulation
The following exact prompt was used to guide the AI assistant in refactoring procedural SQL into SQLAlchemy ORM and conducting a comprehensive security analysis:

```text
Act as a Senior Database Architect and Python Engineer. Refactor the following procedural MySQL database script into a modern, production-grade SQLAlchemy ORM implementation.

Initial Procedural Code:
--------------------------------------------------
import mysql.connector
from mysql.connector import Error

def get_connection():
    """Establish and return a database connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="example_db"
    )

def create_user(db_cursor, username, email):
    """Create a new user safely using parameterized queries."""
    if not username or not email:
        print("Username and email are required.")
        return
    sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
    try:
        db_cursor.execute(sql, (username, email))
        print(f"User '{username}' created successfully.")
    except Error as e:
        print(f"Error creating user: {e}")
--------------------------------------------------

Requirements:
1. Define the User class as a SQLAlchemy declarative model with columns for id (primary key), username, email, and created_at.
2. Show how to create the database table, instantiate an ORM engine/Session, add a new user object, query for that user, update their email, and delete the user using ORM methods.
3. Provide a detailed, technical explanation analyzing why the SQLAlchemy (ORM) implementation is a significantly more professional, maintainable, and secure solution compared to procedural raw SQL string manipulation.
```

---

## 🛡️ Security Analysis & Professional Benefits

### 1. Elimination of SQL Injection (SQLi) Vulnerabilities
In procedural database interaction, engineers frequently fall into the trap of dynamic SQL construction using string concatenation or `%s` formatting (e.g., `f"SELECT * FROM users WHERE username = '{username}'"`). If input sanitization is missed, malicious actors can inject SQL commands (such as `' OR '1'='1`).

SQLAlchemy ORM completely eliminates this attack vector by abstracting database queries into an **Abstract Syntax Tree (AST)**. Query filters (e.g., `session.query(User).filter(User.username == username)`) never format string input directly into SQL text. Instead, SQLAlchemy binds parameters automatically at the database protocol level (`PREPARE` and `EXECUTE`), enforcing strict parameter binding across all database engines.

### 2. Transaction Integrity & Automatic Rollback
Procedural MySQL connector code requires manually managing transaction state across database connection objects (`conn.commit()`, `conn.rollback()`). Failing to handle errors properly can leave database connections hanging or leave tables in an inconsistent partial state.

SQLAlchemy’s `Session` acts as a **Unit of Work** design pattern. It tracks all object state changes (pending insertions, modifications, deletions) in memory and flushes them in a single transaction block. If an error occurs, calling `session.rollback()` safely restores the database to a consistent state.

---

## 🏗️ Abstraction & Maintainability Comparison

| Dimension | Procedural Raw SQL (`procedural_user_manager.py`) | SQLAlchemy ORM (`orm_user_manager.py`) |
| :--- | :--- | :--- |
| **Data Representation** | Tuples/Dictionaries (`user[0]`, `user[1]`) | Python Objects (`user.id`, `user.username`) |
| **Schema Management** | Manual DDL strings (`CREATE TABLE users ...`) | Python Declarative Classes (`User(Base)`) |
| **Database Portability** | Tied to MySQL dialect syntax (`%s` placeholders) | Multi-database support (MySQL, PostgreSQL, SQLite) |
| **Query Safety** | Risk of string format errors & SQLi | Type-safe Python expressions (`User.username == name`) |
| **Maintainability** | Refactoring schema requires editing multiple SQL strings | Single source of truth in `User` model |

---

## 🚀 Execution Instructions

### Running the ORM User Manager
To execute the refactored SQLAlchemy ORM demonstration locally:

```bash
# Execute the SQLAlchemy ORM user manager
python orm_user_manager.py
```

### Output Preview:
```text
Initializing SQLAlchemy ORM Engine...

--- 1. Creating Users ---
Success: User 'nebyu_assefa' created with ID 1.
Success: User 'alice_dev' created with ID 2.

--- 2. Querying User ---
Found User -> ID: 1, Username: nebyu_assefa, Email: nebyu@example.com

--- 3. Updating User Email ---
Success: Updated 'nebyu_assefa' email from 'nebyu@example.com' to 'nebyu.updated@example.com'.

--- 4. Listing All Users ---
--- Total Users (2) ---
ID: 1 | Username: nebyu_assefa | Email: nebyu.updated@example.com | Created: 2026-10-03 12:43:51.907985
ID: 2 | Username: alice_dev | Email: alice@example.com | Created: 2026-10-03 12:43:51.910454

--- 5. Deleting User ---
Success: User 'alice_dev' deleted successfully.

--- 6. Final User List ---
--- Total Users (1) ---
ID: 1 | Username: nebyu_assefa | Email: nebyu.updated@example.com | Created: 2026-10-03 12:43:51.907985
```
