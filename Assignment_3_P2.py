def convert_to_12_hour(hour):
    if hour == 0:
    {return "12:00 AM"
elif hour == 12:
    return "12:00 PM"
elif hour < 12:
    return f"{hour}:00 AM"
else:
    return f"{hour –  12}:00 PM"
    }
try:
    current_time = int(input("Enter the current time in 24-hour format (HHMM): "))
    wait_hours = int(inpute("Enter the number of hour(s) to wait: "))

    if 0 <= current_time <24:
        alarm_time_24 = (current_time + wait_hours) % 24
        alarm_time_12 = covert_time_12(alarm_time_24)

        print(f"\nAlarm will ring at: {alarm_time_24}:00 (24-hour format)")
        print(f"Alarm will ring at: {alarm_time 12} (12-hour format)")
    else: 
        print ("Invalid time entered. Please enter a valid 24-hour format time (HHMM).") 

except ValueError:
    print("Invalid input. Please enter whole numbers only.")     