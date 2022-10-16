from ics import Calendar
from datetime import datetime
import requests


# Check if input is a valid date or not
def is_valid(d):
    try:
        # strptime throw a error if the date doesn't match the pattern %Y-%m-%d
        return len(d) == 10 and datetime.strptime(d, '%Y-%m-%d')

    except ValueError:
        return False

# Check if input is a holiday or not
def is_holiday(input_date, limit):
    if limit <= 0:
        print('Tentativi finiti')
        return
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
            new_date_entry = input('Reinserire una data: ')
            is_holiday(new_date_entry, limit - 1)

    except:
        print("L'anno inserito non è disponibile")
        new_date_entry = input('Reinserire una data: ')
        is_holiday(new_date_entry, limit - 1)


# Enter a date
date_entry = input('Inserire una data YYYY-MM-DD: ')

is_holiday(date_entry, 3)
