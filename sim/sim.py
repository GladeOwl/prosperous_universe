from inventory import Inventory

def simulate_time():
    runtime: int = 24 * 60
    hours: int = 0
    minutes: int = 0
    hour_minutes: int = 0

    while (minutes < runtime):
        minutes += 1
        hour_minutes += 1
        if (hour_minutes == 60):
            hour_minutes = 0
            hours += 1
    
    print(f"Done in {hours}H:{hour_minutes}M ({minutes} minutes).")


if __name__ == "__main__":
    max_weight = 1500
    max_volume = 1500
    inventory = Inventory(max_weight, max_volume)

    simulate_time()