
    
  
def park_vehicle(parking_slots):
    if len(parking_slots) < 20:
        vehicle_number = input("Please enter your vehicle number: ")
        parking_slots.append(vehicle_number)
        print("Vehicle parked successfully.")
    else:
        print("Sorry, parking slots are full.")

def retrieve_vehicle(parking_slots):
    vehicle_number = input("Please enter your vehicle number: ")
    if vehicle_number in parking_slots:
        parking_slots.remove(vehicle_number)
        print("Vehicle retrieved successfully.")
    else:
        print("Vehicle not found in the parking slots.")

def main():
    parking_slots = []

    while True:
        action = input("Do you want to park (P), retrieve (R), or exit (E)? ").upper()
        
        if action == "P":
            park_vehicle(parking_slots)
        elif action == "R":
            retrieve_vehicle(parking_slots)
        elif action == "E":
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please choose P, R, or E.")

if __name__ == "__main__":
    main()
