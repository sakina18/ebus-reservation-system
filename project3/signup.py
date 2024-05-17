from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

# Function to clear input fields
def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmpasswordEntry.delete(0, END)
    check.set(0)

# Function to connect to the database and register the user
def connect_database():
    # Validate input fields
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('ERROR', 'All Fields Are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('ERROR', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('ERROR', 'Please Accept Terms And Conditions')
    else:
        try:
            # Connect to MySQL database
            con = pymysql.connect(host='localhost', user='root', password='12345')
            mycursor = con.cursor()
        except pymysql.Error as e:
            # Handle database connectivity issues
            print("Error:", e)
            messagebox.showerror('ERROR', 'Database Connectivity Issue, Please Try Again ')
            return
        try:
            # Create database and table if they don't exist
            query = 'create database if not exists data1'
            mycursor.execute(query)
            query = 'use data1'
            mycursor.execute(query)
            query = 'create table if not exists data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            # Switch to the existing database
            mycursor.execute('use data1')
        
        # Insert user data into the database
        query = 'insert into data(email,username,password) values(%s,%s,%s)'
        mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get())) 
        con.commit()
        con.close()
        # Show success message, clear input fields, and destroy signup window
        messagebox.showinfo('Success', 'Registration is Successful')   
        clear()
        signup_window.destroy()
        # Import and open login page
        import loginpage1
                
# Function to open the login page
def login_page():
    signup_window.destroy()
    import loginpage1

# Create main window
signup_window = Tk()
signup_window.title('signup page')
signup_window.resizable(False, False)

# Load background image
background = ImageTk.PhotoImage(file='bus2.jpg')
bgLabel = Label(signup_window, image=background)
bgLabel.grid()

# Create frame for form elements
frame = Frame(signup_window, bg='white')
frame.place(x=40, y=200)

# Create heading label
heading = Label(frame, text='CREATE AN ACCOUNT', font=('serif', 20), bg='white', fg='black')
heading.grid(row=0, column=0, padx=10, pady=10)

# Create labels and entry widgets for email, username, password, and confirm password
emailLabel = Label(frame, text='Email', font=('sans', 10, 'bold'), bg='white', fg='black')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
emailEntry = Entry(frame, width=25, font=('sans', 10, 'bold'), fg='black', bg='white')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernameLabel = Label(frame, text='Username', font=('sans', 10, 'bold'), bg='white', fg='black')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
usernameEntry = Entry(frame, width=25, font=('sans', 10, 'bold'), bg='white', fg='black')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

passwordLabel = Label(frame, text='Password', font=('sans', 10, 'bold'), bg='white', fg='black')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
passwordEntry = Entry(frame, width=25, font=('sans', 10, 'bold'), bg='white', fg='black')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

confirmpasswordLabel = Label(frame, text='Confirm Password', font=('sans', 10, 'bold'), bg='white', fg='black')
confirmpasswordLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))
confirmpasswordEntry = Entry(frame, width=25, font=('sans', 10, 'bold'), bg='white', fg='black')
confirmpasswordEntry.grid(row=8, column=0, sticky='w', padx=25)

# Create terms and conditions checkbox
check = IntVar()
termsandconditions = Checkbutton(frame, text='I Agree To The Terms & Conditions', font=('sans', 10, 'bold'),
                                 fg='black', bg='white', activebackground='white', activeforeground='black',
                                 cursor='hand2', variable=check)
termsandconditions.grid(row=9, column=0, padx=10, pady=15)

# Create signup button
signupButton = Button(frame, text='SIGN UP', font=('sans', 10, 'bold'), bg='black', fg='white',
                      activebackground='sky blue', activeforeground='white', width=17, command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

# Create label and button for already have an account
alreadyaccount = Label(frame, text='Already have an account?', font=('sans', 9, 'bold'), bg='white', fg='black')
alreadyaccount.grid(row=11, column=0, sticky='w', pady=10)
loginButton = Button(frame, text='log in', font=('sans', 9, 'bold underline'), fg='blue', bg='white',
                     activebackground='grey', bd='0', activeforeground='blue', cursor='hand2', command=login_page)
loginButton.place(x=150, y=380)

signup_window.mainloop()
