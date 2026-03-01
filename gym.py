from datetime import datetime, timedelta

# -------------------------
# 1. Membership Types
# -------------------------
membership_types = ["Monthly", "Quarterly", "Yearly", "Day-Pass"]

# -------------------------
# 2. Members
# -------------------------
members = []

# Function to add a member
def add_member(member_id, name, membership_type, status="active"):
    if membership_type not in membership_types:
        print(f"Error: Invalid membership type. Choose from {membership_types}")
        return
    member = {
        "id": member_id,
        "name": name,
        "membership_type": membership_type,
        "status": status
    }
    members.append(member)
    print(f"Member {name} added successfully!")

# Function to remove a member
def remove_member(member_id):
    global members
    members = [m for m in members if m["id"] != member_id]
    print(f"Member with ID {member_id} removed successfully!")

# Function to show a member's details
def show_member(member_id):
    for m in members:
        if m["id"] == member_id:
            print(m)
            return
    print("Member not found!")

# Function to display all members
def display_members():
    if not members:
        print("No members yet.")
    for m in members:
        print(m)

# Function to search for a member by name
def search_member(name):
    for m in members:
        if m["name"].lower() == name.lower():
            return m
    print("Member not found!")
    return None

# Function to update a member's subscription status
def update_status(member_id, status):
    for m in members:
        if m["id"] == member_id:
            m["status"] = status
            print(f"Member {m['name']}'s status updated to {status}")
            return
    print("Member not found!")

# Function to show active members only
def show_active_members():
    active = [m for m in members if m["status"] == "active"]
    if not active:
        print("No active members.")
    for m in active:
        print(m)

# -------------------------
# 3. Subscriptions
# -------------------------
subscriptions = []

# Function to add a subscription
def add_subscription(member_id, membership_type, start_date_str):
    member = search_member_by_id(member_id)
    if not member:
        print("Cannot add subscription: member does not exist.")
        return

    # Determine expiration based on membership type
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    if membership_type == "Monthly":
        expiration_date = start_date + timedelta(days=30)
    elif membership_type == "Quarterly":
        expiration_date = start_date + timedelta(days=90)
    elif membership_type == "Yearly":
        expiration_date = start_date + timedelta(days=365)
    elif membership_type == "Day-Pass":
        expiration_date = start_date + timedelta(days=1)
    else:
        print("Invalid membership type")
        return

    subscription = {
        "member_id": member_id,
        "membership_type": membership_type,
        "start_date": start_date,
        "expiration_date": expiration_date
    }
    subscriptions.append(subscription)
    print(f"Subscription added for member ID {member_id}")

# Helper function to get member by ID
def search_member_by_id(member_id):
    for m in members:
        if m["id"] == member_id:
            return m
    return None

# Function to cancel a subscription
def cancel_subscription(member_id):
    global subscriptions
    subscriptions = [s for s in subscriptions if s["member_id"] != member_id]
    print(f"Subscription for member ID {member_id} canceled.")

# Function to show subscription details
def show_subscription(member_id):
    for s in subscriptions:
        if s["member_id"] == member_id:
            print({
                "member_id": s["member_id"],
                "membership_type": s["membership_type"],
                "start_date": s["start_date"].strftime("%Y-%m-%d"),
                "expiration_date": s["expiration_date"].strftime("%Y-%m-%d")
            })
            return
    print("Subscription not found!")

# Function to calculate total revenue (assuming fixed prices)
membership_prices = {
    "Monthly": 50,
    "Quarterly": 140,
    "Yearly": 500,
    "Day-Pass": 10
}

def total_revenue():
    revenue = 0
    today = datetime.today()
    for s in subscriptions:
        if s["expiration_date"] >= today:
            revenue += membership_prices.get(s["membership_type"], 0)
    print(f"Total revenue from active subscriptions: ${revenue}")

# Function to display all subscriptions
def display_subscriptions():
    if not subscriptions:
        print("No subscriptions yet.")
    for s in subscriptions:
        print({
            "member_id": s["member_id"],
            "membership_type": s["membership_type"],
            "start_date": s["start_date"].strftime("%Y-%m-%d"),
            "expiration_date": s["expiration_date"].strftime("%Y-%m-%d")
        })

# -------------------------
# 4. Menu to test functions
# -------------------------
def menu():
    while True:
        print("\n--- Gym Management System ---")
        print("1. Add Member")
        print("2. Remove Member")
        print("3. Show Member Details")
        print("4. Display All Members")
        print("5. Search Member by Name")
        print("6. Update Member Status")
        print("7. Show Active Members")
        print("8. Add Subscription")
        print("9. Cancel Subscription")
        print("10. Show Subscription Details")
        print("11. Display All Subscriptions")
        print("12. Total Revenue")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            id = input("Member ID: ")
            name = input("Name: ")
            mtype = input(f"Membership Type {membership_types}: ")
            add_member(id, name, mtype)
        elif choice == "2":
            id = input("Member ID to remove: ")
            remove_member(id)
        elif choice == "3":
            id = input("Member ID to show: ")
            show_member(id)
        elif choice == "4":
            display_members()
        elif choice == "5":
            name = input("Member name to search: ")
            m = search_member(name)
            if m:
                print(m)
        elif choice == "6":
            id = input("Member ID: ")
            status = input("New status (active/inactive): ")
            update_status(id, status)
        elif choice == "7":
            show_active_members()
        elif choice == "8":
            id = input("Member ID: ")
            mtype = input(f"Membership Type {membership_types}: ")
            start_date = input("Start Date (YYYY-MM-DD): ")
            add_subscription(id, mtype, start_date)
        elif choice == "9":
            id = input("Member ID to cancel subscription: ")
            cancel_subscription(id)
        elif choice == "10":
            id = input("Member ID to show subscription: ")
            show_subscription(id)
        elif choice == "11":
            display_subscriptions()
        elif choice == "12":
            total_revenue()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

# Run the menu
if __name__ == "__main__":
    menu()
