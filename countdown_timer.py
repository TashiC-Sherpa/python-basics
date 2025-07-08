import time
try:
    period = input("Enter the time period: ")
    parts = period.split(":")
    minutes = int(parts[0])
    seconds = int(parts[1])
    total_period = (minutes * 60) + seconds

    while (total_period > 0):
        min, remaining_sec = divmod(total_period, 60)
        print(f"Time remaining: {str(min).zfill(2)}:{str(remaining_sec).zfill(2)}")
        total_period -= 1
        time.sleep(1)

    print("Time's up!")

except ValueError:
    print("Error, Please enter numbers only")
