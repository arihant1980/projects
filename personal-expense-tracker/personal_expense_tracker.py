import csv
import os

EXPENSE_FILE = "expenses.csv"

expenses = []
monthly_budget = 0.0


# -----------------------------
# Load expenses from CSV file
# -----------------------------
def load_expenses():
    global expenses

    if not os.path.exists(EXPENSE_FILE):
        return

    try:
        with open(EXPENSE_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    expenses.append({
                        "date": row["date"],
                        "category": row["category"],
                        "amount": float(row["amount"]),
                        "description": row["description"]
                    })
                except (ValueError, KeyError):
                    print("Skipping invalid row in file.")

    except Exception as e:
        print("Error loading expenses:", e)


# -----------------------------
# Save expenses to CSV
# -----------------------------
def save_expenses():

    try:
        with open(EXPENSE_FILE, mode="w", newline="", encoding="utf-8") as file:

            fieldnames = ["date", "category", "amount", "description"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for exp in expenses:
                writer.writerow(exp)

        print("Expenses saved successfully.")

    except Exception as e:
        print("Error saving expenses:", e)


# -----------------------------
# Add Expense
# -----------------------------
def add_expense():

    date = input("Enter date (YYYY-MM-DD): ").strip()

    category = input("Enter category (Food, Travel, etc.): ").strip()

    try:
        amount = float(input("Enter amount spent: "))
    except ValueError:
        print("Invalid amount.")
        return

    description = input("Enter description: ").strip()

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully.")


# -----------------------------
# View Expenses
# -----------------------------
def view_expenses():

    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expense List ---")

    for exp in expenses:

        if not all(key in exp for key in ["date", "category", "amount", "description"]):
            print("Incomplete expense entry found. Skipping.")
            continue

        print(
            "Date:", exp["date"],
            "| Category:", exp["category"],
            "| Amount:", exp["amount"],
            "| Description:", exp["description"]
        )


# -----------------------------
# Track Budget
# -----------------------------
def track_budget():

    global monthly_budget

    if monthly_budget == 0:
        try:
            monthly_budget = float(input("Enter your monthly budget: "))
        except ValueError:
            print("Invalid budget amount.")
            return

    total_expenses = sum(exp["amount"] for exp in expenses)

    print("\nTotal Expenses:", total_expenses)
    print("Monthly Budget:", monthly_budget)

    if total_expenses > monthly_budget:
        print("You have exceeded your budget!")
    else:
        remaining = monthly_budget - total_expenses
        print("You have", remaining, "left for the month.")


# -----------------------------
# Menu
# -----------------------------
def menu():

    while True:

        print("\n===== Personal Expense Tracker =====")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            track_budget()

        elif choice == "4":
            save_expenses()

        elif choice == "5":
            save_expenses()
            print("Expenses saved. Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")


# -----------------------------
# Main
# -----------------------------
def main():

    load_expenses()

    menu()


if __name__ == "__main__":
    main()