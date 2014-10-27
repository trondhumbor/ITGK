__author__ = "Tsh"

# very database, much primarykey

birthdays = {
    "22 nov ": ["Lars", "Mathias"],
    "10 des ": "Elle",
    "30 okt ": ["Veronica", "Rune"],
    "12 jan ": "Silje",
    "31 okt ": "Willy",
    "8 jul ": ["Brage", "Øystein"],
    "1 mar ": "Nina"
}

def add_birthday_to_date ( date , name ):
    try:
        birthdays [ date ]. append ( name )
    except AttributeError:
        birthdays[date] = [birthdays[date], name]
    except KeyError:
        birthdays.update({date: [name]})

if __name__ == "__main__":
    for birthday in birthdays:
        print(birthday, birthdays[birthday])
    add_birthday_to_date ("12 jan", "Sindre")
    add_birthday_to_date ("9 feb", "Lillian")
    for birthday in birthdays:
        print(birthday, birthdays[birthday])

