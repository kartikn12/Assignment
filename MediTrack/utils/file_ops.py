import os
import csv

INVOICE_DIR = "data/invoices"
os.makedirs(INVOICE_DIR, exist_ok=True)

def save_invoice_txt(patient_name, amount):
    path = f"{INVOICE_DIR}/{patient_name}.txt"
    with open(path, "w") as f:
        f.write(f"Patient Name: {patient_name}\n")
        f.write(f"Total Amount: Rs. {amount}\n")

def save_invoice_csv(patient_name, amount):
    path = f"{INVOICE_DIR}/billing_history.csv"
    file_exists = os.path.isfile(path)

    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Patient Name", "Amount"])
        writer.writerow([patient_name, amount])
