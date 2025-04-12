from app.config import get_db_connection

class basic_info:
    @staticmethod
    def save_basic_info(user_id, name, age_range, gender, known_allergy, chronic_disease, disability, emergency_contact_info):
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO basic_info (
                user_id, name, age_range, gender, known_allergy,
                chronic_disease, disability, emergency_contact_info
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                name = VALUES(name),
                age_range = VALUES(age_range),
                gender = VALUES(gender),
                known_allergy = VALUES(known_allergy),
                chronic_disease = VALUES(chronic_disease),
                disability = VALUES(disability),
                emergency_contact_info = VALUES(emergency_contact_info)
        """
        cursor.execute(query, (user_id, name, age_range, gender, known_allergy,
                               chronic_disease, disability, emergency_contact_info))
        conn.commit()
        conn.close()

    @staticmethod
    def get_basic_info(user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM basic_info WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        data = cursor.fetchone()

        conn.close()
        return data

    @staticmethod
    def update_basic_info(user_id, data):
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            UPDATE basic_info
            SET
                name = %s,
                age_range = %s,
                gender = %s,
                known_allergy = %s,
                chronic_disease = %s,
                disability = %s,
                emergency_contact_info = %s
            WHERE user_id = %s
        """
        cursor.execute(query, (
            data.get('name'), data.get('age_range'), data.get('gender'),
            data.get('known_allergy'), data.get('chronic_disease'),
            data.get('disability'), data.get('emergency_contact_info'), user_id
        ))
        conn.commit()
        conn.close()
