from database import get_connection

class Appointment:
    def __init__(self, patient_id, doctor, status, date):
        self.patient_id = patient_id
        self.doctor = doctor
        self.status = status
        self.date = date

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO appointments
               (patient_id, doctor, status, visit_date)
               VALUES (%s, %s, %s, %s)""",
            (self.patient_id, self.doctor, self.status, self.date)
        )
        conn.commit()
        conn.close()
