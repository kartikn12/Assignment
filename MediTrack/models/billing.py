class Billing:
    TAX_RATE = 0.05

    def __init__(self, consultation, medicines):
        if consultation == "" or medicines == "":
            raise ValueError("Charges cannot be empty")

        consultation = float(consultation)
        medicines = float(medicines)

        if consultation < 0 or medicines < 0:
            raise ValueError("Charges cannot be negative")

        self.consultation = consultation
        self.medicines = medicines

    def calculate_total(self):
        subtotal = self.consultation + self.medicines
        tax = subtotal * self.TAX_RATE
        return round(subtotal + tax, 2)
