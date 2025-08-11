def convert_to_12_hour(hour):
    if hour == 0:
        return "12:00 AM"
    elif hour == 12:
        return "12:00 PM"
    elif hour < 12:
        return f"{hour}:00 AM"
    else:
        return f"{hour - 12}:00 PM"
    
try:
    current_time = int(input("Enter the current time in 24-hour format (0-23): "))
    wait_hours = int(input("Enter the number of hour(s) to wait: "))

    if 0 <= current_time < 24:
        alarm_time_24 = (current_time + wait_hours) % 24
        alarm_time_12 = convert_to_12_hour(alarm_time_24)

        print(f"\nAlarm will ring at:")
        print(f" - {alarm_time_24}:00 (24-hour format)")
        print(f" - {alarm_time_12} (12-hour format)")
    else: 
        print ("Invalid time entered. Please enter a valid 24-hour format time (0-23).") 

except ValueError:
    print("Invalid input. Please enter whole numbers only.")     