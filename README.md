# Python Expense Tracker

A simple CLI application to track expenses using SQLite.

## Features

- Add, view, and delete expenses
- Stores expenses with date, description, and amount
- Unit tests with pytest
- Test coverage with coverage.py

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/nagarajumatta/python-expense-tracker.git
   cd python-expense-tracker
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv env
   .\env\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

- Add an expense:
  ```
  python expense_tracker.py add 2025-07-17 "Lunch" 12.5
  ```

- View expenses:
  ```
  python expense_tracker.py view
  ```

- Delete an expense:
  ```
  python expense_tracker.py delete <ID>
  ```

## Testing

- Run tests:
  ```
  pytest
  ```

- Measure coverage:
  ```
  coverage run -m pytest
  coverage report
  ```

## License

MIT
