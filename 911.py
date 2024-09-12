from datetime import datetime

def days_until_911():
    today = datetime.now()
    current_year = today.year
    
    # Következő 9/11 dátumának meghatározása
    next_911 = datetime(current_year, 9, 11)
    
    # Ha a mai nap után van a szeptember 11, akkor a jelenlegi évben
    if today < next_911:
        delta = next_911 - today
    else:
        # Ha már elmúlt az idei szeptember 11, akkor jövőre lesz a következő
        next_911 = datetime(current_year + 1, 9, 11)
        delta = next_911 - today
    
    # Ha ma van szeptember 11
    if today.month == 9 and today.day == 11:
        print("Ma 9/11 van!")
    else:
        print(f"{delta.days} nap van hátra a következő 9/11-hez.")

days_until_911()
