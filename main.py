import datetime, bday_messages

today = datetime.date.today()
my_next_birthday = datetime.date(2023,11,13)

days_away = my_next_birthday - today

if today == my_next_birthday:
    print(random_message)
else:
    print(f"My next birthday is {days_away} days away from today!")


