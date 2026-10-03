#!/usr/bin/python3
"""
Procedural Database User Manager using MySQL Connector.
Demonstrates raw SQL functions for database operations.
"""
import mysql.connector
from mysql.connector import Error


def get_connection():
    """Establish and return a database connection."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword",
            database="example_db"
        )
        return connection
    except Error as e:
        print(f"Connection error: {e}")
        return None


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


def get_user_by_username(db_cursor, username):
    """Retrieve user record by username."""
    if not username:
        print("Username is required.")
        return None
    sql = "SELECT id, username, email FROM users WHERE username = %s"
    try:
        db_cursor.execute(sql, (username,))
        user = db_cursor.fetchone()
        if user:
            print(f"Found User -> ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
            return user
        else:
            print(f"User '{username}' not found.")
            return None
    except Error as e:
        print(f"Error querying user: {e}")
        return None


def update_user_email(db_cursor, username, new_email):
    """Update a user's email address."""
    if not username or not new_email:
        print("Username and new email are required.")
        return
    sql = "UPDATE users SET email = %s WHERE username = %s"
    try:
        db_cursor.execute(sql, (new_email, username))
        if db_cursor.rowcount > 0:
            print(f"Updated email for '{username}' to '{new_email}'.")
        else:
            print(f"User '{username}' not found or email unchanged.")
    except Error as e:
        print(f"Error updating user email: {e}")


def delete_user(db_cursor, username):
    """Delete a user by username."""
    if not username:
        print("Username is required.")
        return
    sql = "DELETE FROM users WHERE username = %s"
    try:
        db_cursor.execute(sql, (username,))
        if db_cursor.rowcount > 0:
            print(f"User '{username}' deleted successfully.")
        else:
            print(f"User '{username}' not found.")
    except Error as e:
        print(f"Error deleting user: {e}")


def list_users(db_cursor):
    """List all users in the database."""
    sql = "SELECT id, username, email FROM users"
    try:
        db_cursor.execute(sql)
        users = db_cursor.fetchall()
        print("--- User List ---")
        for u in users:
            print(f"ID: {u[0]} | Username: {u[1]} | Email: {u[2]}")
        return users
    except Error as e:
        print(f"Error listing users: {e}")
        return []


if __name__ == "__main__":
    print("Procedural User Manager Module Loaded.")
