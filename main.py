from ics import Calendar
from datetime import datetime
import requests

# Check if input is a valid date or not
def is_valid(d):
    try:
        if len(d) == 10:
            # strptime throw a error if the date doesn't match the pattern %Y-%m-%d
            datetime.strptime(d, '%Y-%m-%d')
            return True
        else: return False

    except ValueError:
        return False

# Check if input is a holiday or not
def is_holiday(input_date):
    input_year = input_date[:4]
    url = f"https://giorni-festivi.eu/ical/italia/{input_year}/"

    try:
        if is_valid(input_date):
            calendar = Calendar(requests.get(url).text)
            found = False
            for e in calendar.events:
                date_festival = e.begin.format("YYYY-MM-DD")
                name_festival = e.name
                if input_date == date_festival:
                    found = True
                    print(date_festival, name_festival)
                    break
                
            if not found:
                print(input_date, 'giorno lavorativo')
        else:
            print('Data non valida, usa il formato: YYYY-MM-DD')
    except:
        print("L'anno inserito non è disponibile")

# Enter a date
date_entry = input('Inserire una data YYYY-MM-DD: ')

# Reenter a date and limit count
count = 0
limit = 3
while not is_valid(date_entry):
    if count < limit:
        date_entry = input('Reinserire una data YYYY-MM-DD: ')
        count += 1
    else:
        print('Tentativi finiti')
        break


# calling the function
is_holiday(date_entry)






