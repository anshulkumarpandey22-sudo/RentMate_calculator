def calculate_rent():
    print("=== Easy Rent Calculator ===")
    names = [n.strip() for n in input("Enter roommate names (comma-separated): ").split(",") if n.strip()]
    
    if not names:
        print("No valid names entered.")
    else:
        rent = float(input("Enter total rent amount: $"))
        utilities = float(input("Enter total utilities amount: $"))
        
        total = rent + utilities
        per_person = total / len(names)
        
        print(f"\nTotal Expenses: ${total:.2f}")
        print(f"Each of the {len(names)} roommates owes: ${per_person:.2f}")
        
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    calculate_rent()
    def calculate_rent():
        print("=== Easy Rent Calculator ===")
    names = [n.strip() for n in input("Enter roommate names (comma-separated): ").split(",") if n.strip()]
    
    if not names:
        print("No valid names entered.")
    else:
        rent = float(input("Enter total rent amount: $"))
        utilities = float(input("Enter total utilities amount: $"))
        
        total = rent + utilities
        per_person = total / len(names)
        
        print(f"\nTotal Expenses: ${total:.2f}")
        print(f"Each of the {len(names)} roommates owes: ${per_person:.2f}")
        
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    calculate_rent()
