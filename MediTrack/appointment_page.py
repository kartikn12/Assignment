import tkinter as tk
from tkinter import messagebox
import mysql.connector
import datetime

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="kartik",
        database="meditrack"
    )

def appointment_window():
    win = tk.Toplevel()
    win.title("Appointment Management")
    win.geometry("550x400")

    tk.Label(win, text="Add Appointment", font=("Arial", 14)).pack()

    patient_id = tk.Entry(win)
    doctor = tk.Entry(win)
    status = tk.Entry(win)

    for lbl, entry in [("Patient ID", patient_id),
                       ("Doctor", doctor),
                       ("Status", status)]:
        tk.Label(win, text=lbl).pack()
        entry.pack()

    def add_appointment():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """INSERT INTO appointments
                (patient_id, doctor, status, visit_date)
                VALUES (%s,%s,%s,%s)""",
                (int(patient_id.get()),
                 doctor.get(),
                 status.get(),
                 datetime.date.today())
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Appointment Added")
            load_appointments()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Appointment",
              command=add_appointment).pack(pady=5)

    # ---------- APPOINTMENT LIST ----------
    tk.Label(win, text="Appointments", font=("Arial", 12)).pack(pady=5)
    listbox = tk.Listbox(win, width=70)
    listbox.pack()

    def load_appointments():
        listbox.delete(0, tk.END)
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """SELECT p.name, a.doctor, a.status, a.visit_date
               FROM appointments a
               JOIN patients p ON a.patient_id = p.id"""
        )
        for row in cur.fetchall():
            listbox.insert(tk.END, row)
        conn.close()

    load_appointments()

