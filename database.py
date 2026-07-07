import sqlite3

DATABASE = "history.db"


def create_table():
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        url TEXT,

        prediction TEXT,

        confidence REAL,

        risk TEXT,

        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()
    conn.close()


def save_prediction(url, prediction, confidence, risk):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history(url,prediction,confidence,risk)

        VALUES(?,?,?,?)
        """,
        (
            url,
            prediction,
            confidence,
            risk
        )
    )

    conn.commit()

    conn.close()


def get_history():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        url,
        prediction,
        confidence,
        risk,
        date

    FROM history

    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows