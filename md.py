import datetime
import matplotlib.pyplot as plt

print("Vehicle Fuel and Maintenance Tracker\n")

# basic data
vehicle_name = input("Vehicle name/model: ")
vehicle_type = input("Vehicle type (Car/Bike/etc.): ")
fuel_capacity = float(input("Fuel tank capacity (liters): "))
last_maintenance = input("Last maintenance date (YYYY-MM-DD): ")

# date conversion
try:
    last_maint_date = datetime.datetime.strptime(last_maintenance, "%Y-%m-%d").date()
except:
    print("Invalid date entered, using today's date.")
    last_maint_date = datetime.date.today()

total_distance = 0
total_fuel = 0
eff_history = []      # to store efficiency of each trip

# main menu loop
while True:
    print("\nMenu:")
    print("1. Add Trip")
    print("2. Check Fuel Efficiency")
    print("3. Maintenance Status")
    print("4. Fuel Efficiency Chart")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    # add trip
    if choice == "1":
        distance = float(input("Distance travelled (km): "))
        fuel_used = float(input("Fuel used (liters): "))

        if fuel_used > 0:
            efficiency = distance / fuel_used
            print(f"Trip Efficiency: {efficiency:.2f} km/l")
            eff_history.append(efficiency)
        else:
            print("Fuel used must be greater than 0.")
            continue

        total_distance += distance
        total_fuel += fuel_used

    # show overall efficiency
    elif choice == "2":
        if total_fuel > 0:
            avg = total_distance / total_fuel
            print(f"Overall Efficiency: {avg:.2f} km/l")
        else:
            print("No trip data recorded yet.")

    # maintenance check
    elif choice == "3":
        next_due = last_maint_date + datetime.timedelta(days=180)
        days_left = (next_due - datetime.date.today()).days

        print(f"Last Maintenance: {last_maint_date}")
        print(f"Next Due: {next_due}")

        if days_left > 0:
            print(f"{days_left} days remaining.")
        else:
            print("Maintenance overdue.")

    # fuel efficiency chart
    elif choice == "4":
        if len(eff_history) == 0:
            print("No trip data to display chart.")
        else:
            trips = list(range(1, len(eff_history) + 1))
            plt.plot(trips, eff_history, marker='o')
            plt.xlabel("Trip No.")
            plt.ylabel("Efficiency (km/l)")
            plt.title("Fuel Efficiency Chart")
            plt.grid(True)
            plt.show()

    # exit
    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid option.")