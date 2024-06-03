from tkinter import *
from tkinter import messagebox

def login():
    username = Username.get()
    passwd = password.get()
    if username == "Username" or passwd == "Password":
        messagebox.showwarning("Input error", "Please enter both username and password")
    elif username == "wakaama20" and passwd == "tigeress7":
        messagebox.showinfo("Login", f"Welcome {username}")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def on_entry_click(event, entry, placeholder, is_password=False):
    """Function to handle entry field click event"""
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.config(fg='black')
        if is_password:
            entry.config(show='*')

def on_focusout(event, entry, placeholder, is_password=False):
    """Function to handle entry field focus out event"""
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')
        if is_password:
            entry.config(show='')

root = Tk()
root.title('wakaama results')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width * 0.5)
window_height = int(screen_height * 0.5)
root.geometry(f'{window_width}x{window_height}')

frame = Frame(root, bg="white")
frame.pack(pady=20)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 20, 'bold'))
heading.grid(row=0, column=0, columnspan=2, pady=10)

# Username
Username = Entry(frame, width=25, fg='grey', bg='white', font=('Microsoft Yahei UI Light', 11))
Username.insert(0, 'Username')
Username.grid(row=1, column=0, padx=10, pady=5)
Username.bind('<FocusIn>', lambda event: on_entry_click(event, Username, 'Username'))
Username.bind('<FocusOut>', lambda event: on_focusout(event, Username, 'Username'))

# Password
password = Entry(frame, width=25, fg='grey', bg="white", font=('Microsoft Yahei UI Light', 11))
password.insert(0, 'Password')
password.grid(row=2, column=0, padx=10, pady=5)
password.bind('<FocusIn>', lambda event: on_entry_click(event, password, 'Password', is_password=True))
password.bind('<FocusOut>', lambda event: on_focusout(event, password, 'Password', is_password=True))

# Login Button
Button(frame, text='Enter', bg='#57a1f8', fg='white', command=login).grid(row=3, column=0, pady=10)

file_list = Listbox(frame, width=50, height=10)
file_list.grid(row=4, column=0, pady=10)

root.mainloop()
