from flask import Flask, render_template, request, redirect, url_for, flash
import qrcode
import os
import uuid
import sqlite3
from datetime import datetime
from urllib.parse import urlparse

app = Flask(__name__)
app.secret_key = "local-secret-key"

# Paths
QR_FOLDER = "static/qrcodes"
DB_NAME = "database.db"

# Ensure QR folder exists
os.makedirs(QR_FOLDER, exist_ok=True)

# ---------- DATABASE ----------
def get_db():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS qr_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            filename TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ---------- URL VALIDATION ----------
def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and parsed.netloc != ""

# ---------- ROUTES ----------
@app.route("/", methods=["GET", "POST"])
def index():
    qr_image = None

    if request.method == "POST":
        url = request.form.get("url", "").strip()

        if not is_valid_url(url):
            flash("Please enter a valid URL starting with http:// or https://")
            return redirect(url_for("index"))

        filename = f"{uuid.uuid4()}.png"
        filepath = os.path.join(QR_FOLDER, filename)

        img = qrcode.make(url)
        img.save(filepath)

        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO qr_codes (url, filename, created_at) VALUES (?, ?, ?)",
            (url, filename, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        conn.commit()
        conn.close()

        qr_image = filepath

    return render_template("index.html", qr_image=qr_image)

@app.route("/history")
def history():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM qr_codes ORDER BY id DESC")
    data = cur.fetchall()
    conn.close()
    return render_template("history.html", data=data)

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT filename FROM qr_codes WHERE id=?", (id,))
    file = cur.fetchone()

    if file:
        path = os.path.join(QR_FOLDER, file[0])
        if os.path.exists(path):
            os.remove(path)

    cur.execute("DELETE FROM qr_codes WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for("history"))

# ---------- MAIN ----------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
