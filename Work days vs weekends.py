def daysOfWeek(days):
    days = days/7
    weekEnds = days * 2
    workDays = days * 5
    days = days * 7
    weekEnds = round(weekEnds)
    workDays = round(workDays)
    days = round(days)
    if days <= 6:
        if days > 1:
            weekEnds = 1
        workDays = days
    print("Days of the week:", days, "work days:", workDays, "weekends days:", weekEnds,"\n")
    

def loop():
    while True:
        days = input("Number of days? ")
        try:
            days = int(days)
        except:
            try:
                days = float(days)                
            except:
                print("Invalid input\n")
                break
        daysOfWeek(days)
    loop()

def main():
    loop()
    
main()
