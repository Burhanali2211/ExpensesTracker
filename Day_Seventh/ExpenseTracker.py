import datetime
import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description="", date=None):
        if date is None:
            date = datetime.date.today().isoformat()
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }
        self.expenses.append(expense)
        print(f"\n✅ Expense added: ₹{amount} for {category} on {date}. {description}")

    def view_expenses(self, filter_category=None, filter_date=None):
        filtered_expenses = self.expenses
        
        if filter_category:
            filtered_expenses = [e for e in filtered_expenses if e["category"] == filter_category]

        if filter_date:
            filtered_expenses = [e for e in filtered_expenses if e["date"] == filter_date]

        if not filtered_expenses:
            print("\nNo expenses found.")
            return

        total = 0
        print("\n📋 Your Expenses:")
        for expense in filtered_expenses:
            print(f"- ₹{expense['amount']} on {expense['date']} for {expense['category']}: {expense['description']}")
            total += expense['amount']

        print(f"\n💰 Total: ₹{total}")

    def view_total_spent(self):
        total_spent = sum(expense['amount'] for expense in self.expenses)
        print(f"\n💸 Total amount spent so far: ₹{total_spent}")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.expenses, file, indent=4)
        print(f"\n✅ Expenses saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                self.expenses = json.load(file)
            print(f"\n📂 Expenses loaded from {filename}")
        except FileNotFoundError:
            print(f"\n❌ File {filename} not found. Starting with an empty tracker.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.load_from_file("expenses.json")

    while True:
        print("\n=======================")
        print("🌟 Expense Tracker Menu 🌟")
        print("=======================")
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Save and Exit")

        choice = input("\nEnter your choice (1/2/3/4): ")

        if choice == "1":
            try:
                amount = float(input("\nEnter the amount (₹): "))
                category = input("Enter the category: ")
                description = input("Enter a description (optional): ")
                date = input("Enter the date (YYYY-MM-DD, optional): ") or None
                tracker.add_expense(amount, category, description, date)
            except ValueError:
                print("\n❌ Invalid input. Please try again.")

        elif choice == "2":
            category_filter = input("\nFilter by category (leave blank for no filter): ") or None
            date_filter = input("Filter by date (YYYY-MM-DD, leave blank for no filter): ") or None
            tracker.view_expenses(category_filter, date_filter)

        elif choice == "3":
            tracker.view_total_spent()

        elif choice == "4":
            tracker.save_to_file("expenses.json")
            print("\n👋 Goodbye! Your expenses have been saved.")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")
