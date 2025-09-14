import datetime

# Predefined festivals (you can edit or add more)
festivals = {
    "Diwali": "2025-10-20",
    "Christmas": "2025-12-25",
    "New Year": "2026-01-01",
    "Pongal": "2026-01-15"
}

def add_festival():
    name = input("Enter festival name: ").strip()
    date_str = input("Enter festival date (YYYY-MM-DD): ").strip()
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")  # validate date
        festivals[name] = date_str
        print(f"✅ Festival '{name}' added!")
    except ValueError:
        print("❌ Invalid date format! Use YYYY-MM-DD.")

def delete_festival():
    name = input("Enter festival name to delete: ").strip()
    if name in festivals:
        del festivals[name]
        print(f"🗑️ Festival '{name}' deleted!")
    else:
        print("❌ Festival not found.")

def view_festivals():
    if not festivals:
        print("No festivals saved.")
    else:
        print("\n📅 Saved Festivals:")
        for name, date_str in festivals.items():
            print(f" - {name}: {date_str}")

def check_reminders():
    today = datetime.date.today()
    print(f"\n📌 Today: {today}")
    found = False
    for name, date_str in festivals.items():
        festival_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        diff = (festival_date - today).days
        if diff == 0:
            print(f"🎉 Today is {name}!")
            found = True
        elif 0 < diff <= 7:
            print(f"🔔 {name} is in {diff} days ({date_str})")
            found = True
    if not found:
        print("No upcoming festivals in the next 7 days.")

def festival_bot():
    while True:
        print("\n=== Festival Reminder Bot ===")
        print("1. View all festivals")
        print("2. Add a festival")
        print("3. Delete a festival")
        print("4. Check reminders")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_festivals()
        elif choice == "2":
            add_festival()
        elif choice == "3":
            delete_festival()
        elif choice == "4":
            check_reminders()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    festival_bot()
