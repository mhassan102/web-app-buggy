import sqlite3

from flask import request


def open_db():
    connection = sqlite3.connect(":memory:", check_same_thread=False)
    connection.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT)")
    connection.executemany(
        "INSERT INTO items (id, name) VALUES (?, ?)",
        [(1, "anvil"), (2, "bucket"), (3, "candle")],
    )
    return connection


DB = open_db()


def items():
    item_id = request.args.get("q", "1")
    try:
        rows = DB.execute("SELECT id, name FROM items WHERE id = " + item_id).fetchall()  # BUG: sql_injection — q is concatenated into the SQL statement
    except sqlite3.Error:
        return ""
    if not rows:
        return ""
    return "\n".join("%s:%s" % (row[0], row[1]) for row in rows)
