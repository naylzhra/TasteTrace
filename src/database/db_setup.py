import mysql.connector


# cara runnya ikutin ini:
# mysql -u root -p
# masukin password
# CREATE USER 'taste_trace'@'localhost' IDENTIFIED BY 'tastetrace';
# CREATE DATABASE taste_trace_db;
# GRANT ALL PRIVILEGES ON taste_trace_db.* TO 'taste_trace'@'localhost';
# FLUSH PRIVILEGES;
# trs bisa lgsg jalanin file ini trs seeder.py
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='taste_trace',
            password='tastetrace',
            database='taste_trace_db',
            auth_plugin= 'mysql_native_password'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def create_tables():
    conn = get_db_connection()
    if conn is None:
        return

    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS CustomerReview (
        review_id INT AUTO_INCREMENT PRIMARY KEY,
        reviewer_name VARCHAR(100),
        review_date DATE,
        review_text TEXT NOT NULL,
        rate INT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()