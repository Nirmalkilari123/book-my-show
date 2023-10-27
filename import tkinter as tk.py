import tkinter as tk

def select_seat(seat_type, seat_number):
    if seat_type == "Standard":
        standard_seats.remove(seat_number)
    else:
        premium_seats.remove(seat_number)
    update_seat_display()

def update_seat_display():
    standard_label.config(text="Standard Seats: " + str(standard_seats))
    premium_label.config(text="Premium Seats: " + str(premium_seats))

standard_seats = [f"ST-{i}" for i in range(1, 11)]
premium_seats = [f"PR-{i}" for i in range(1, 6)]

app = tk.Tk()
app.title("Book My Seat")

standard_label = tk.Label(app, text="Standard Seats: " + str(standard_seats))
standard_label.pack()

premium_label = tk.Label(app, text="Premium Seats: " + str(premium_seats))
premium_label.pack()

for seat in standard_seats + premium_seats:
    button = tk.Button(app, text=seat, command=lambda s=seat: select_seat(s.split('-')[0], s))
    button.pack()

app.mainloop()