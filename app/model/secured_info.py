from app.config import get_db_connection

class secured_info:
    @staticmethod
    def save_secured_info(user_id, full_name, medical_history, medication_in_use, doctor_details, exact_age):
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO secured_info (
                user_id, full_name, medical_history, medication_in_use,
                doctor_details, exact_age
            ) VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                full_name = VALUES(full_name),
                medical_history = VALUES(medical_history),
                medication_in_use = VALUES(medication_in_use),
                doctor_details = VALUES(doctor_details),
                exact_age = VALUES(exact_age)
        """
        cursor.execute(query, (user_id, full_name, medical_history, medication_in_use, doctor_details, exact_age))
        conn.commit()
        conn.close()

    @staticmethod
    def get_secured_info(user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM secured_info WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        data = cursor.fetchone()

        conn.close()
        return data

    @staticmethod
    def update_secured_info(user_id, data):
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            UPDATE secured_info
            SET
                full_name = %s,
                medical_history = %s,
                medication_in_use = %s,
                doctor_details = %s,
                exact_age = %s
            WHERE user_id = %s
        """
        cursor.execute(query, (
            data.get('full_name'), data.get('medical_history'),
            data.get('medication_in_use'), data.get('doctor_details'),
            data.get('exact_age'), user_id
        ))
        conn.commit()
        conn.close()
