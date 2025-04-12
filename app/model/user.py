from app.config import get_db_connection
import bcrypt

class user:
    @staticmethod
    def create_user(username, email, phone_number, password):
        conn = get_db_connection()
        cursor = conn.cursor()

        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        query = "INSERT INTO users VALUES (%s, %s, %s, %s)"
        
        cursor.execute(query, (username, email, phone_number, password_hash))
        conn.commit()
        conn.close()

    @staticmethod
    def get_user_by_email(email):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        conn.close()
        return user
