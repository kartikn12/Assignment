import tkinter as tk
from tkinter import messagebox
from models.billing import Billing
from utils.file_ops import save_invoice_txt, save_invoice_csv

def billing_window():
    win = tk.Toplevel()
    win.title("Billing & Payment")
    win.geometry("350x300")

    tk.Label(win, text="Patient Name").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    tk.Label(win, text="Consultation Charges").pack()
    consult_entry = tk.Entry(win)
    consult_entry.pack()

    tk.Label(win, text="Medicine Charges").pack()
    med_entry = tk.Entry(win)
    med_entry.pack()

    def generate_bill():
        try:
            bill = Billing(
                consult_entry.get(),
                med_entry.get()
            )

            total = bill.calculate_total()

            save_invoice_txt(name_entry.get(), total)
            save_invoice_csv(name_entry.get(), total)

            messagebox.showinfo(
                "Success",
                f"Bill Generated\nTotal: Rs. {total}"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(
        win,
        text="Generate Bill",
        command=generate_bill
    ).pack(pady=10)
