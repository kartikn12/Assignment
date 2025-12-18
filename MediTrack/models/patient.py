from database import get_connection

class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO patients (name, age, disease) VALUES (%s, %s, %s)",
            (self.name, self.age, self.disease)
        )
        conn.commit()
        conn.close()
