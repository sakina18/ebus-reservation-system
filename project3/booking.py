from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk

# Validation function for booking details
def validate_booking():
    if source_dropdown.get() == '' or destination_dropdown.get() == '' or cal.get_date() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    elif source_dropdown.get() == destination_dropdown.get():
        messagebox.showerror('Error', 'Please choose different Source or Destination')
    else:
        messagebox.showinfo('Success', 'Your Bus has been Booked')
        clear_entries()

# Function to clear the entries after successful booking
def clear_entries():
    source_dropdown.set('')
    destination_dropdown.set('')
    cal.set_date('')

# Create main Tkinter window
booking_window = Tk()
booking_window.title('Booking Page')
booking_window.resizable(False, False)

# Load background image
background = ImageTk.PhotoImage(file='bus2.jpg')
bgLabel = Label(booking_window, image=background)
bgLabel.grid()

# Create a frame to contain the booking elements
frame = Frame(booking_window, bg='white')
frame.place(x=40, y=200)

# Heading label for the booking section
heading = Label(frame, text='Book Your Bus', font=('serif', 20), bg='white', fg='black')
heading.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Choices for source and destination dropdowns
choices = ['Srinagar', 'Baramulla', 'Anantnag', 'Kupwara', 'Ganderbal']

# Source dropdown and label
source_label = Label(frame, text='Source:', font=('sans', 10, 'bold'), bg='white', fg='black')
source_label.grid(row=1, column=0, padx=25, pady=5, sticky='w')
source_dropdown = ttk.Combobox(frame, values=choices, width=25, font=('sans',10))
source_dropdown.grid(row=1, column=1, padx=25, pady=5)

# Destination dropdown and label
destination_label = Label(frame, text='Destination:', font=('sans', 10, 'bold'), bg='white', fg='black')
destination_label.grid(row=2, column=0, padx=25, pady=5, sticky='w')
destination_dropdown = ttk.Combobox(frame, values=choices, width=25, font=('sans',10))
destination_dropdown.grid(row=2, column=1, padx=25, pady=5)

# Date calendar and label
date_label = Label(frame, text='Date of Travel:', font=('sans', 10, 'bold'), bg='white', fg='black')
date_label.grid(row=3, column=0, padx=25, pady=5, sticky='w')
cal = DateEntry(frame, selectmode='day', width=15, font=('sans',10))
cal.grid(row=3, column=1, padx=25, pady=5, sticky='w')

# Continue button for booking
continue_button = Button(frame, text='Continue', font=('sans', 10, 'bold'), bg='green', fg='white',
                         activebackground='white', activeforeground='white', width=17, command=validate_booking)
continue_button.grid(row=4, column=0, columnspan=2, pady=10)


booking_window.mainloop()
