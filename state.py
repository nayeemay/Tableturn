# state.py

# Table tracking dictionary
tables = {
    1: {"status": "Available", "capacity": 2, "customer": None},
    2: {"status": "Available", "capacity": 4, "customer": None},
    3: {"status": "Available", "capacity": 6, "customer": None},
    4: {"status": "Available", "capacity": 4, "customer": None},
}

waitlist = []
reservations = []
analytics = {"total_served": 0}