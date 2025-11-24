# Personal Expense Tracker

expenses = []
budget = 0
user_name = ""
user_age = 0

def user_details():
    global user_name
    global user_age
    print("Enter Your Details:")
    user_name = input("Your Name : ")
    user_age = input("Your Age : ")
    print(f"Welcome {user_name}! Let's manage your expenses")


def set_budget():
    global budget
    budget = float(input("Enter your monthly budget : "))
    print("Budget set successfully!")


def add_expense():
    name = input("Enter expense name : ")
    amount = float(input("Enter amount : ₹"))
    expenses.append({"name": name, "amount": amount})
    print("Expense added successfully!")
    check_budget()


def view_expenses():
    if expenses==[]:
        print("No expenses recorded yet.")
        return
    print(f"All Expenses of User: {user_name}")
    for i in range(len(expenses)):
        print(f"{i+1}. {expenses[i]["name"]} - ₹{expenses[i]["amount"]}")


def total_expense():
    total = 0
    for exp in expenses:
        total=total+exp["amount"]
    print(f"Total Expense : ₹{total}")
    return total


def check_budget():
    total = total_expense()
    if total > budget:
        print("WARNING! You have exceeded your budget!")


def edit_expense():
    view_expenses()
    if expenses==[]:
        return
    num = int(input("Enter expense number to edit : "))
    num=num-1
    if 0 <= num < len(expenses):
        expenses[num]["name"] = input("Enter new name : ")
        expenses[num]["amount"] = float(input("Enter new amount : ₹"))
        print("Expense updated!")
    else:
        print("Invalid choice!")


def delete_expense():
    view_expenses()
    if expenses==[]:
        return
    num = int(input("Enter expense number to delete : "))
    num=num-1
    if 0 <= num < len(expenses):
        expenses.pop(num)
        print("Expense deleted!")
    else:
        print("Invalid choice!")


def search_expense():
    key = input("Enter expense name to search : ")
    found = False
    for exp in expenses:
        if key.lower() == exp["name"].lower():
            print(f"{exp['name']} - ₹{exp['amount']}")
            found = True
    if not found:
        print("No match found!")


user_details()
set_budget()
while True:
    print("===== Expense Tracker Menu =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Search Expense")
    print("6. Total Expense")
    print("7. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        edit_expense()
    elif choice == 4:
        delete_expense()
    elif choice == 5:
        search_expense()
    elif choice == 6:
        total_expense()
    elif choice == 7:
        print(f"Goodbye {user_name}! Stay within budget!")
        break
    else:
        print("Invalid choice! Try again")