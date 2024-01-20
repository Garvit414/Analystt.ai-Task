import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, amount, category):
        today = datetime.date.today()
        date_str = today.strftime("%Y-%m-%d")

        if date_str not in self.expenses:
            self.expenses[date_str] = []

        self.expenses[date_str].append({"amount": amount, "category": category})
        print(f"Expense of ${amount} in the category '{category}' added for {date_str}.")

    def view_expenses(self):
        print("\nExpense Tracker:")
        for date, expenses_list in self.expenses.items():
            print(f"\nDate: {date}")
            for expense in expenses_list:
                print(f"  Amount: ${expense['amount']}  |  Category: {expense['category']}")

    def view_spending_pattern(self):
        print("\nSpending Pattern:")
        for date, expenses_list in self.expenses.items():
            total_amount = sum(expense['amount'] for expense in expenses_list)
            print(f"{date}: Total Spending - ${total_amount}")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending Pattern")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter the expense amount: $"))
            category = input("Enter the expense category: ")
            expense_tracker.add_expense(amount, category)
        elif choice == "2":
            expense_tracker.view_expenses()
        elif choice == "3":
            expense_tracker.view_spending_pattern()
        elif choice == "4":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
