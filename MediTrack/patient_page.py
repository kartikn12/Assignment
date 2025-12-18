import tkinter as tk
from tkinter import messagebox
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="kartik",
        database="meditrack"
    )

def patient_window():
    win = tk.Toplevel()
    win.title("Patient Management")
    win.geometry("500x400")

    tk.Label(win, text="Add Patient", font=("Arial", 14)).pack()

    name = tk.Entry(win)
    age = tk.Entry(win)
    disease = tk.Entry(win)

    for lbl, entry in [("Name", name), ("Age", age), ("Disease", disease)]:
        tk.Label(win, text=lbl).pack()
        entry.pack()

    def add_patient():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO patients (name, age, disease) VALUES (%s,%s,%s)",
                (name.get(), int(age.get()), disease.get())
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Patient Added")
            load_patients()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Patient", command=add_patient).pack(pady=5)

    # ---------- PATIENT LIST ----------
    tk.Label(win, text="Patient List", font=("Arial", 12)).pack(pady=5)
    listbox = tk.Listbox(win, width=60)
    listbox.pack()

    def load_patients():
        listbox.delete(0, tk.END)
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, disease FROM patients")
        for row in cur.fetchall():
            listbox.insert(tk.END, row)
        conn.close()

    load_patients()
