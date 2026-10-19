# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ").strip()
while not name:
    print("Passenger name cannot be empty.")
    name = input("Enter passenger name: ").strip()

while True:
    try:
        distance = float(input("Enter distance (km): "))
        if distance > 0:
            break
        print("Distance must be greater than 0.")
    except ValueError:
        print("Enter a valid number for distance.")

while True:
    try:
        passengers = int(input("Enter number of passengers: "))
        if passengers > 0:
            break
        print("Number of passengers must be a positive whole number.")
    except ValueError:
        print("Enter a positive whole number.")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
