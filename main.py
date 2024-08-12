/app
    /templates
        index.html
        create_post.html
    app.py
    database.py
requirements.txt
from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3
import uuid
from datetime import datetime

#Application
app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('social_media.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM Posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/create_post', methods=('GET', 'POST'))
def create_post():
    if request.method == 'POST':
        user_id = request.form['user_id']
        title = request.form['title']
        description = request.form['description']
        cost = request.form['cost']
        category = request.form['category']
        variants = request.form['variants']
        location = request.form['location']
        image_url = request.form['image_url']
        theme = request.form['theme']
        post_id = str(uuid.uuid4())
        created_at = datetime.now()


@app.route('/feedback')
def feedback():
    conn = get_db_connection()
    total_liked_posts = conn.execute('''
        SELECT COUNT(*) FROM PostPlatforms WHERE likes > 0
    ''').fetchone()[0]

    platforms_usage = conn.execute('''
        SELECT platform_id, COUNT(*) AS usage_count FROM PostPlatforms
        GROUP BY platform_id
        ORDER BY usage_count DESC
    ''').fetchall()

    conn.close()

#Database
def initialize_database():
    conn = sqlite3.connect('social_media.db')
    cursor = conn.cursor()
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id TEXT PRIMARY KEY,
        username TEXT,
        email TEXT,
        password_hash TEXT,
        twofa_enabled BOOLEAN,
        created_at TIMESTAMP,
        updated_at TIMESTAMP
    );
