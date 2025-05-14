def calculate_water_intake(weight, age):
    if age < 12:
        return round(weight * 30 / 1000, 2)
    elif age > 55:
        return round(weight * 40 / 1000, 2)
    else:
        return round(weight * 35 / 1000, 2)

def get_reminder_interval(water_intake):
    if water_intake < 1.5:
        return "Every 4 hours"
    elif water_intake < 2.5:
        return "Every 3 hours"
    else:
        return "Every 2 hours"

def recommend_water_temperature(age):
    if age > 55:
        return "Lukewarm water recommended"
    elif age < 30:
        return "Cool water recommended"
    else:
        return "Room temperature water recommended"

def main():
    try:
        weight = input("Enter your weight in kg: ")
        age = input("Enter your age: ")

        if not weight or not age:
            raise ValueError("Weight and Age cannot be empty.")
        weight = float(weight)
        age = int(age)
        if weight <= 0 or age <= 0:
            raise ValueError("Weight and Age must be positive numbers.")

        water_needed = calculate_water_intake(weight, age)
        interval = get_reminder_interval(water_needed)
        temp_advice = recommend_water_temperature(age)

        print(f"\n✅ Recommended daily water intake: {water_needed} liters")
        print(f"🔔 Reminder interval: {interval}")
        print(f"💧 Water temperature advice: {temp_advice}")

    except ValueError as ve:
        print(f"❌ Error: {ve}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
