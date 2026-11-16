# resto.py
from handlers import (
    view_tables,
    add_reservation,
    view_waitlist,
    assign_table,
    release_table,
    add_to_waitlist,
    seat_from_waitlist,
    cancel_reservation,
    search_customer,
    view_analytics,
    reset_system,
    export_summary
)

def main():
    actions = {
        "1": ("View Tables", view_tables),
        "2": ("Add Reservation", add_reservation),
        "3": ("View Waitlist", view_waitlist),
        "4": ("Assign Table", assign_table),
        "5": ("Release Table", release_table),
        "6": ("Add to Waitlist", add_to_waitlist),
        "7": ("Seat from Waitlist", seat_from_waitlist),
        "8": ("Cancel Reservation", cancel_reservation),
        "9": ("Search Customer", search_customer),
        "10": ("View Analytics", view_analytics),
        "11": ("Reset System", reset_system),
        "12": ("Export Summary", export_summary),
    }

    while True:
        print("\n===== TABLETURN RESTAURANT MANAGEMENT =====")
        for k, (label, _) in actions.items():
            print(f"{k:>2}. {label}")
        print("13. Exit")
        print("-" * 42)

        choice = input("Select an option (1-13): ").strip()
        
        if choice == "13":
            print("Thank you for using TABLETURN!")
            break
        elif choice in actions:
            actions[choice][1]()
        else:
            print("Invalid choice. Enter 1-13.")

if __name__ == "__main__":
    main()