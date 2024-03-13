from tkinter import *
from tkinter import messagebox
import pyperclip
import Pass_gen


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pwd():
    pwd = Pass_gen.Password()
    generated_password = pwd.pass_gen()
    pass_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    user = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure none of the fields are empty!")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Details you entered:\nEmail: {user}\n"
                                                                     f"Password: {password}\nClick 'OK' to save?")

        if is_ok:
            with open("data.txt", "a") as saved_pwd:
                saved_pwd.write(f"{website} | {user} | {password}\n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager App")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_text_label = Label(text="Website:")
website_text_label.grid(column=0, row=1)
email_txt_label = Label(text="Email/Username:")
email_txt_label.grid(column=0, row=2)
pass_txt_label = Label(text="Password:")
pass_txt_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3, sticky="EW")

# Buttons
generate_button = Button(text="Generate Password", command=gen_pwd)
generate_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
