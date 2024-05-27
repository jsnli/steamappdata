from flask import Flask
import os
import psycopg
import json
from dotenv import load_dotenv

if os.path.isfile('./.env'):
    load_dotenv()

user = os.environ['POSTGRES_USER']
host = os.environ['POSTGRES_HOST']
password = os.environ['POSTGRES_PASSWORD']
name = os.environ['POSTGRES_DATABASE']

def get_connection():
    conn = psycopg.connect(f"host={host} dbname={name} user={user} password={password}")
    return conn

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>index()</p>"

@app.route("/search/<name>", methods=['GET'])
def get_game(name):
    conn = get_connection()
    cur = conn.cursor()

    query = "SELECT * FROM Games WHERE Name ILIKE %s"
    name_pattern = f"%{name}%"
    cur.execute(query, (name_pattern,))

    result = []
    applist = cur.fetchall()
    for app in applist:
        result.append({
            "id": app[0],
            "name": app[1],
            "last_modified": app[2]
        })
    

    conn.commit()
    cur.close()
    conn.close()

    return result
