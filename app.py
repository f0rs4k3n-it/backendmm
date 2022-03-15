import sqlite3
from flask import Flask, jsonify, app
from app import app
CVSINFO = {
     'name': 'matteo',
    'surname': 'massai'
}


@app.route("/")
def api_all():
    return jsonify(CVSINFO)


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

app = Flask(__name__)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4444, debug=True)
    create_connection(r"pythonsqlite.db")
