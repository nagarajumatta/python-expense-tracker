import os
import sqlite3
import pytest
from db import DB_NAME, init_db, add_expense, get_expenses, delete_expense

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup: create a fresh database
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    init_db()
    yield
    # Teardown: remove database
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

def test_add_and_get_expense():
    add_expense("2025-07-17", "Lunch", 12.5)
    expenses = get_expenses()
    assert len(expenses) == 1
    assert expenses[0][1] == "2025-07-17"
    assert expenses[0][2] == "Lunch"
    assert expenses[0][3] == 12.5

def test_delete_expense():
    add_expense("2025-07-17", "Coffee", 3.0)
    expenses = get_expenses()
    expense_id = expenses[0][0]
    delete_expense(expense_id)
    expenses = get_expenses()
    assert len(expenses) == 0
