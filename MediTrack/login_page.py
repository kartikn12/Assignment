import tkinter as tk
from tkinter import messagebox
from database import get_connection
from models.user import User

current_user = None   # GLOBAL USER OBJECT

def login_window(root, open_dashboard):

    win = tk.Toplevel(root)
    win.title("Login")
    win.geometry("300x200")

    tk.Label(win, text="Username").pack()
    username_entry = tk.Entry(win)
    username_entry.pack()

    tk.Label(win, text="Password").pack()
    password_entry = tk.Entry(win, show="*")
    password_entry.pack()

    def login():
        global current_user

        try:
            conn = get_connection()
            cur = conn.cursor(dictionary=True)

            cur.execute(
                "SELECT username, role FROM users WHERE username=%s AND password=%s",
                (username_entry.get(), password_entry.get())
            )

            user_data = cur.fetchone()
            conn.close()

            if user_data:
                current_user = User(
                    user_data["username"],
                    user_data["role"]
                )
                messagebox.showinfo("Success", "Login Successful")
                win.destroy()
                open_dashboard()
            else:
                messagebox.showerror("Error", "Invalid credentials")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Login", command=login).pack(pady=10)
