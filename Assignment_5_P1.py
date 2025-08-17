def general():
    years = int(input("Enter the number of years: "))
    
    total_rainfall = 0.0
    total_months = 0

    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        for month in range(1, 13):
            rainfall = float(input(f" Enter rainfall (in inches) for the month {month}: "))
            total_rainfall += rainfall
            total_months += 1
    
    average_rainfall = total_rainfall / total_months 
    print("\nRainfall Summary")
    print(f"\nTotal number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")   

general()
