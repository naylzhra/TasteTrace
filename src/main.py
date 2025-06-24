import collections, sys
from mysql.connector import Error
from database.db_setup import get_db_connection          # unchanged helper
from model.fuzzy_match import extract_mentions
import math

def fetch_reviews():
    try:
        with get_db_connection() as con, con.cursor(dictionary=True) as cur:
            cur.execute("SELECT review_text, rate FROM CustomerReview")
            return [(row["review_text"], row["rate"]) for row in cur.fetchall()]
    except Error as err:
        sys.exit(f"MySQL error: {err}")

def analyse():
    stats = collections.defaultdict(lambda: [0, 0])

    for text, rate in fetch_reviews():
        rate = rate or 0
        for item in extract_mentions(text):
            stats[item][0] += 1
            stats[item][1] += rate

    for item, (n, total) in sorted(stats.items(), key=lambda x: x[0]):
        avg = total / n if n else 0
        avg_str = f"{avg:.1f}".rstrip("0").rstrip(".")
        print(f"{item}:\n  - Overall review: {avg_str}\n  - Mentions: {n}\n")

if __name__ == "__main__":
    analyse()
