
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


# Function to validate login credentials and perform login


def login_user():
    if EmailEntry.get() == '' or passentry.get() == '':
        # Validate if username and password fields are not empty
        messagebox.showerror('Error', 'All Fields are Required')
    else:
        try:
            # Connect to MySQL database
            con = pymysql.connect(host='localhost', user='root', password='12345')
            mycursor = con.cursor()
        except pymysql.Error as e:
            # Handle database connectivity issues
            print("Error:", e)
            messagebox.showerror('ERROR', 'Connection is not Established try again ')
            return
        
        # Execute SQL query to fetch user with entered username and password
        query = 'use data1'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (EmailEntry.get(), passentry.get()))
        
        # Fetch one row from the result
        row = mycursor.fetchone()
        
        if row == None:
            # If no user found, show error message
            messagebox.showerror('Error', 'Invalid Username or Password')
        else:
            # If user found, show success message
            messagebox.showinfo('Welcome', 'Login is Successful')
            signup_window.destroy()
            import booking

# Function to navigate to signup page
def sign_page():
    signup_window.destroy()
    import signup

# Create main window
signup_window = Tk()
signup_window.title('Login Page')
signup_window.resizable(False, False)

# Load background image
background = ImageTk.PhotoImage(file='bus2.jpg')
bgLabel = Label(signup_window, image=background)
bgLabel.grid()

# Create frame for login form
frame = Frame(signup_window, bg='white')
frame.place(x=40, y=200)

# Create heading label
heading = Label(frame, text='USER LOGIN', font=('serif', 25), bg='white', fg='black')
heading.grid(row=0, column=0, padx=10, pady=10)

# Create labels and entry widgets for username and password
EmailLabel = Label(frame, text='Username', font=('sans', 10, 'bold'), bg='white', fg='black')
EmailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
EmailEntry = Entry(frame, width=25, font=('sans', 10, 'bold'), fg='black', bg='white')
EmailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernameLabel = Label(frame, text='Password', font=('sans', 10, 'bold'), bg='white', fg='black')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
passentry = Entry(frame, width=25, font=('sans', 10, 'bold'), bg='white', fg='black')
passentry.grid(row=4, column=0, sticky='w', padx=25)

# Create login button
loginbutton = Button(frame, text='Login', font=('sans', 10, 'bold'), bg='blue', fg='white',
                     activebackground='sky blue', activeforeground='white', width=17, command=login_user)
loginbutton.grid(row=6, column=0, pady=10)

# Create label and button for navigating to signup page
alreadyaccount = Label(frame, text='Dont have an account?', font=('sans', 9, 'bold'), bg='white', fg='black')
alreadyaccount.grid(row=11, column=0, sticky='w', pady=10)
newaccountButton = Button(signup_window, text='Create new one', font=('sans', 9, 'bold underline'),
                          fg='blue', bg='white', activebackground='grey',
                          bd='0', activeforeground='blue', cursor='hand2', command=sign_page)
newaccountButton.place(x=175, y=425)


signup_window.mainloop()
