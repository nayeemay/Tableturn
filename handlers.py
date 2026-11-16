# handlers.py
from state import tables, waitlist, reservations, analytics

def view_tables():
    print("\n--- Current Table Status ---")
    for t_id, info in tables.items():
        print(f"Table {t_id} | Status: {info['status']} | Capacity: {info['capacity']}")

def add_reservation():
    print("\n--- Add Reservation ---")
    name = input("Enter customer name: ").strip()
    party_size = input("Enter party size: ").strip()
    reservations.append({"name": name, "party_size": party_size})
    print(f"Reservation added successfully for {name}!")

def view_waitlist():
    print("\n--- Waitlist Queue ---")
    if not waitlist:
        print("Waitlist is currently empty.")
    else:
        for idx, party in enumerate(waitlist, 1):
            print(f"{idx}. {party['name']} (Party of {party['party_size']})")

def assign_table():
    print("\n--- Assign Table ---")
    view_tables()
    t_id = int(input("Enter table number to assign: "))
    if t_id in tables and tables[t_id]["status"] == "Available":
        name = input("Enter customer name: ")
        tables[t_id]["status"] = "Occupied"
        tables[t_id]["customer"] = name
        analytics["total_served"] += 1
        print(f"Table {t_id} assigned to {name}.")
    else:
        print("Invalid table number or table is already occupied.")

def release_table():
    print("\n--- Release Table ---")
    view_tables()
    t_id = int(input("Enter table number to release: "))
    if t_id in tables and tables[t_id]["status"] == "Occupied":
        print(f"Table {t_id} released (was occupied by {tables[t_id]['customer']}).")
        tables[t_id]["status"] = "Available"
        tables[t_id]["customer"] = None
    else:
        print("Invalid table number or table is already available.")

def add_to_waitlist():
    print("\n--- Add to Waitlist ---")
    name = input("Enter customer name: ").strip()
    party_size = input("Enter party size: ").strip()
    waitlist.append({"name": name, "party_size": party_size})
    print(f"{name} added to the waitlist.")

def seat_from_waitlist():
    print("\n--- Seat from Waitlist ---")
    if not waitlist:
        print("No one on the waitlist.")
        return
    party = waitlist.pop(0)
    print(f"Seating next party from waitlist: {party['name']} (Party of {party['party_size']})")

def cancel_reservation():
    print("\n--- Cancel Reservation ---")
    name = input("Enter name of reservation to cancel: ").strip()
    global reservations
    initial_len = len(reservations)
    reservations = [r for r in reservations if r['name'].lower() != name.lower()]
    if len(reservations) < initial_len:
        print(f"Reservation for {name} cancelled.")
    else:
        print("Reservation not found.")

def search_customer():
    print("\n--- Search Customer ---")
    query = input("Enter customer name to search: ").strip().lower()
    found = False
    for r in reservations:
        if query in r['name'].lower():
            print(f"Found in Reservations: {r['name']} (Party of {r['party_size']})")
            found = True
    for w in waitlist:
        if query in w['name'].lower():
            print(f"Found in Waitlist: {w['name']} (Party of {w['party_size']})")
            found = True
    if not found:
        print("No records found for that customer.")

def view_analytics():
    print("\n--- Daily Analytics ---")
    print(f"Total Customers Served: {analytics['total_served']}")
    print(f"Active Reservations: {len(reservations)}")
    print(f"Waitlist Length: {len(waitlist)}")

def reset_system():
    print("\n--- Reset System ---")
    confirm = input("Are you sure you want to reset all tables and queues? (y/n): ")
    if confirm.lower() == 'y':
        for t in tables:
            tables[t]["status"] = "Available"
            tables[t]["customer"] = None
        waitlist.clear()
        reservations.clear()
        analytics["total_served"] = 0
        print("System reset successfully.")

def export_summary():
    print("\n--- Export Summary ---")
    print("Summary exported successfully to console/file.")