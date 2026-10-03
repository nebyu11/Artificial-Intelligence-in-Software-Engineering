#!/usr/bin/python3
"""
SQLAlchemy ORM User Manager.
Refactored object-oriented version of the procedural MySQL user manager.
Demonstrates declarative model definition, session-based CRUD operations,
and robust error handling.
"""
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Declarative Base Definition
Base = declarative_base()


class User(Base):
    """
    SQLAlchemy Declarative Model representing the 'users' table.
    Encapsulates table schema and pythonic row mapping.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"


def get_engine(db_url="sqlite:///:memory:"):
    """
    Create and return a SQLAlchemy database engine.
    Supports MySQL (e.g. mysql+mysqldb://user:pwd@localhost/example_db) or SQLite.
    """
    return create_engine(db_url, echo=False)


def create_session(engine):
    """Create and return a new ORM session."""
    Session = sessionmaker(bind=engine)
    return Session()


def init_db(engine):
    """Create all declarative tables in the database."""
    Base.metadata.create_all(engine)


# --- ORM CRUD Functions ---

def create_user(session, username, email):
    """Create and persist a new user using ORM Session."""
    if not username or not email:
        print("Error: Username and email are required.")
        return None
    try:
        new_user = User(username=username, email=email)
        session.add(new_user)
        session.commit()
        print(f"Success: User '{username}' created with ID {new_user.id}.")
        return new_user
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Database Error creating user '{username}': {e}")
        return None


def get_user_by_username(session, username):
    """Query a user by username using ORM filter."""
    if not username:
        print("Error: Username is required for query.")
        return None
    try:
        user = session.query(User).filter(User.username == username).first()
        if user:
            print(f"Found User -> ID: {user.id}, Username: {user.username}, Email: {user.email}")
            return user
        else:
            print(f"Notice: User '{username}' not found.")
            return None
    except SQLAlchemyError as e:
        print(f"Database Error querying user '{username}': {e}")
        return None


def update_user_email(session, username, new_email):
    """Update a user's email address object attribute."""
    if not username or not new_email:
        print("Error: Username and new email are required.")
        return False
    try:
        user = session.query(User).filter(User.username == username).first()
        if user:
            old_email = user.email
            user.email = new_email
            session.commit()
            print(f"Success: Updated '{username}' email from '{old_email}' to '{new_email}'.")
            return True
        else:
            print(f"Notice: Cannot update email. User '{username}' not found.")
            return False
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Database Error updating email for '{username}': {e}")
        return False


def delete_user(session, username):
    """Delete a user object using ORM Session."""
    if not username:
        print("Error: Username is required for deletion.")
        return False
    try:
        user = session.query(User).filter(User.username == username).first()
        if user:
            session.delete(user)
            session.commit()
            print(f"Success: User '{username}' deleted successfully.")
            return True
        else:
            print(f"Notice: Cannot delete. User '{username}' not found.")
            return False
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Database Error deleting user '{username}': {e}")
        return False


def list_users(session):
    """Retrieve and list all User objects."""
    try:
        users = session.query(User).order_by(User.id).all()
        print(f"--- Total Users ({len(users)}) ---")
        for u in users:
            print(f"ID: {u.id} | Username: {u.username} | Email: {u.email} | Created: {u.created_at}")
        return users
    except SQLAlchemyError as e:
        print(f"Database Error listing users: {e}")
        return []


if __name__ == "__main__":
    # Demonstration of complete ORM Workflow
    print("Initializing SQLAlchemy ORM Engine...")
    engine = get_engine("sqlite:///:memory:")
    init_db(engine)
    session = create_session(engine)

    print("\n--- 1. Creating Users ---")
    create_user(session, "nebyu_assefa", "nebyu@example.com")
    create_user(session, "alice_dev", "alice@example.com")

    print("\n--- 2. Querying User ---")
    get_user_by_username(session, "nebyu_assefa")

    print("\n--- 3. Updating User Email ---")
    update_user_email(session, "nebyu_assefa", "nebyu.updated@example.com")

    print("\n--- 4. Listing All Users ---")
    list_users(session)

    print("\n--- 5. Deleting User ---")
    delete_user(session, "alice_dev")

    print("\n--- 6. Final User List ---")
    list_users(session)
