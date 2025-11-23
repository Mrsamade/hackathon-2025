from flask import Flask, render_template, request, jsonify, g
import sqlite3
import os

app = Flask(__name__)

DATABASE = os.path.join(os.path.dirname(__file__), "match.db")


# ------------------ DB HELPERS ------------------

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT,
            bio TEXT,
            image_url TEXT
        );

        CREATE TABLE IF NOT EXISTS swipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            swiper_id INTEGER,
            swiped_id INTEGER,
            direction TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

    # -------- SEED PROFILES (SHORT BIOS) --------
    existing = db.execute("SELECT COUNT(*) FROM profiles").fetchone()[0]
    if existing == 0:
        seed_profiles = [
            (
                "Alex",
                "Computer Science",
                "I'm 21 and a tidy, quiet flatmate who loves cooking and keeping a friendly home.",
                "https://t4.ftcdn.net/jpg/04/67/95/73/360_F_467957383_3yRd5rVS1KcK6mjVNXaNwnGkxe2JOqDu.jpg",
            ),
            (
                "Sam",
                "Engineering",
                "I'm 22, outgoing and active, and keep shared spaces clean while staying flexible with noise.",
                "https://media.gettyimages.com/id/1438969575/photo/smiling-young-male-college-student-wearing-headphones-standing-in-a-classroom.jpg?s=612x612&w=gi&k=20&c=SpIONFFVzrC2OpgxeC2GEpUs0mDQxjw8xn9Z-gfGs5c=",
            ),
            (
                "Maya",
                "Psychology",
                "I'm 20, organised and calm, and prefer a tidy, peaceful living environment.",
                "https://t3.ftcdn.net/jpg/05/60/70/68/360_F_560706812_0GNEvn3tqo6OVQtE0JIvlwZx8fu6S2SR.jpg",
            ),
            (
                "Omar",
                "Business Management",
                "I'm 22, social and easygoing, and enjoy cooking and relaxing with flatmates.",
                "https://t4.ftcdn.net/jpg/04/07/56/25/360_F_407562548_JxUfwmEJBDVpJ1ZquXOPvaYWhnQqwOW6.jpg",
            ),
            (
                "Chloe",
                "Biology",
                "I'm 19, tidy and studious, and enjoy a quiet, clean home with considerate flatmates.",
                "https://media.gettyimages.com/id/1773215539/photo/university-student-portrait-in-campus.jpg?s=612x612&w=gi&k=20&c=YrSJCtU2kj9ofxZ7wsQXB2oMxeemn1K-p-emgFc4Ggg=",
            ),
        ]

        db.executemany(
            "INSERT INTO profiles (name, subject, bio, image_url) VALUES (?, ?, ?, ?)",
            seed_profiles,
        )
        db.commit()


# ------------------ ROUTES ------------------

@app.route("/")
def index():
    db = get_db()
    profiles = db.execute("SELECT * FROM profiles ORDER BY id").fetchall()
    return render_template("default.html", profiles=profiles)


@app.route("/swipe", methods=["POST"])
def swipe():
    data = request.get_json()
    swiper_id = data.get("swiper_id", 1)
    swiped_id = data["swiped_id"]
    direction = data["direction"]

    db = get_db()
    db.execute(
        "INSERT INTO swipes (swiper_id, swiped_id, direction) VALUES (?, ?, ?)",
        (swiper_id, swiped_id, direction),
    )
    db.commit()

    return jsonify({"status": "ok"})


# ------------------ MAIN ------------------

if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)
