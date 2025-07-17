import argparse
from db import init_db, add_expense, get_expenses, delete_expense

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("date", help="Date of expense (YYYY-MM-DD)")
    add_parser.add_argument("description", help="Description of expense")
    add_parser.add_argument("amount", type=float, help="Amount spent")

    view_parser = subparsers.add_parser("view", help="View all expenses")

    del_parser = subparsers.add_parser("delete", help="Delete an expense by ID")
    del_parser.add_argument("id", type=int, help="Expense ID to delete")

    args = parser.parse_args()
    init_db()

    if args.command == "add":
        add_expense(args.date, args.description, args.amount)
        print("Expense added.")
    elif args.command == "view":
        expenses = get_expenses()
        for exp in expenses:
            print(f"ID: {exp[0]}, Date: {exp[1]}, Description: {exp[2]}, Amount: {exp[3]}")
    elif args.command == "delete":
        delete_expense(args.id)
        print("Expense deleted.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
