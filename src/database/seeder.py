

import sys, pathlib
import mysql.connector
from db_setup import get_db_connection


def load_and_execute(sql_path: pathlib.Path):
    conn = get_db_connection()
    if conn is None:
        sys.exit("❌ Failed to connect to MySQL.")

    cursor = conn.cursor()
    statement = []

    with sql_path.open(encoding="utf-8") as fh:
        for raw_line in fh:
            line = raw_line.strip()

            # skip comments / blanks
            if not line or line.startswith("--"):
                continue

            statement.append(line)

            if line.endswith(";"):
                sql = " ".join(statement)
                try:
                    cursor.execute(sql)
                except mysql.connector.Error as err:
                    print(f"⚠ MySQL error: {err}\n   ➜ Offending SQL (truncated): {sql[:120]}…")
                statement = []

    conn.commit()
    cursor.close()
    conn.close()
    print("✔ All statements executed and committed.")

def clean_db():
    conn = get_db_connection()
    if conn is None:
        return
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE CustomerReview")
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    sql_file = pathlib.Path(__file__).with_name("db.sql")

    if not sql_file.exists():
        sys.exit(f"❌ SQL file not found: {sql_file}")
    clean_db()
    load_and_execute(sql_file)
