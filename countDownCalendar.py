from tkinter import Tk, Canvas, simpledialog
from datetime import date, datetime

def get_event():
    list_events = []
    with open('data.py') as file:
        for line in file:
            if line == '':
                continue
            line = line.rstrip("\n")
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events

def day_between_dates(date1, date2):
    time_between = date1-date2
    return time_between.days

def read_from_user():
    user_input = simpledialog.askstring("Calendar", "Type the event and the date. (Format: Eventname,dd/mm/yy)")
    if user_input is not None:
        with open('data.py', 'a') as file:
            file.write(user_input)
        return user_input.split(",")

def add_event_to_canvas(event, canvas, vertical_space):
    event_name = event[0]
    days_until = day_between_dates(event[1], today)
    display = '%s : %s Days Until' % (event_name, days_until)
    c.create_text(100, vertical_space, anchor='w', fill='red', text=display, font='Verdana 25 italic')
    return vertical_space + 50

def add_new_event():
    new_event = read_from_user()
    if new_event:
        event_date = datetime.strptime(new_event[1].strip(), "%d/%m/%y").date()
        new_event[1] = event_date
        events.append(new_event)
        global vertical_space
        vertical_space = add_event_to_canvas(new_event, c, vertical_space)

import tkinter
window = Tk()
header = tkinter.Frame(window)
header.pack()
c = Canvas(window, width=1000, height=800, bg='black')
c.pack()
header_text = c.create_text(100, 50, anchor='w', fill='lightblue', text='My Calendar',font='Courier 35 bold underline')
add_event_button = tkinter.Button(header, text="Add Event", command=add_new_event)
add_event_button.grid(row=0, column=1, padx=10)

events = get_event()
today = date.today()
vertical_space = 150

for event in events:
    vertical_space = add_event_to_canvas(event, c, vertical_space)

window.mainloop()
