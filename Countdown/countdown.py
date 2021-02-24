from tkinter import Tk, Canvas
from datetime import date, datetime


vertical_space = 100


def get_events():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)
        return list_events


def days_between(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]


root = Tk()
c = Canvas(root, width=800, bg='Black')
c.pack()
c.create_text(100, 50, anchor='w', fill='White', font='Arial 29 bold underline', text='Countdown Calendar')

events = get_events()
today = date.today()

events.sort(key=lambda x: x[1])
for event in events:
    event_name = event[0]
    days_until = days_between(event[1], today)
    display = f'It is {days_until} days until {event_name}'
    c.create_text(100, vertical_space ,anchor='w', fill='White', font='Arial 28 bold', text=display)

    vertical_space += 30

root.mainloop()