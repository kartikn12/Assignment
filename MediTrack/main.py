import tkinter as tk
from patient_page import patient_window
from appointment_page import appointment_window
from billing_page import billing_window

root = tk.Tk()
root.title("MediTrack - Main Menu")
root.geometry("300x200")

tk.Label(root, text="MediTrack", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Patient Management",
          width=25,
          command=patient_window).pack(pady=5)

tk.Button(root, text="Appointment Management",
          width=25,
          command=appointment_window).pack(pady=5)
tk.Button(
    root,
    text="Billing",
    command=billing_window
).pack()

root.mainloop()

