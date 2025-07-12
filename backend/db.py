import sqlite3
import os

def get_db_connection():
    conn = sqlite3.connect('graphical_auth.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(base_dir, 'schema.sql')  # this handles path correctly
    with open(schema_path) as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()