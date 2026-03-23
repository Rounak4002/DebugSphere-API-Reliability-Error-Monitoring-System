from flask import Flask, request, jsonify, render_template
import sqlite3
from logger import log_request

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/')
def dashboard():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY id DESC")
    logs = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', logs=logs)

@app.route('/api/test', methods=['GET', 'POST'])
def test_api():
    try:
        data = {"message": "API working fine"}
        status = 200
        return jsonify(data), status
    except Exception as e:
        status = 500
        return jsonify({"error": str(e)}), status
    finally:
        log_request(request.path, request.method, status)

if __name__ == '__main__':
    app.run(debug=True)
