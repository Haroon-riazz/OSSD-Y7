import tkinter as tk
from tkinter import messagebox

USERS_FILE = "users.txt"


# login reading from file
def read_file():
    """Read all stored username:password pairs into a dictionary."""
    users = {}
    try:
        with open(USERS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line and ":" in line:
                    username, password = line.split(":", 1)
                    users[username] = password
    except FileNotFoundError:
        pass
    return users


def write_file(username, password):
    """Append a new username:password pair to the file."""
    with open(USERS_FILE, "a") as file:
        file.write(f"{username}:{password}\n")


def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        messagebox.showwarning("Input Error", "Username and password cannot be empty!")
        return

    users = read_file()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", f"Welcome back, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


def signup():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        messagebox.showwarning("Input Error", "Username and password cannot be empty!")
        return

    users = read_file()

    if username in users:
        messagebox.showerror("Signup Failed", "Username already exists.")
        return

    write_file(username, password)
    messagebox.showinfo("Success", "Account created successfully! You can now log in.")
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def main():
    root.mainloop()


root = tk.Tk()
root.title("Login System")
root.geometry("300x250")

tk.Label(root, text="Username").pack(pady=(20, 0))
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=10)
tk.Button(root, text="Sign Up", command=signup).pack(pady=5)

if __name__ == "__main__":
    main()



root.mainloop()