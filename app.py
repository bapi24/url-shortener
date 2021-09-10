#!/usr/bin/env python3
import random
import string
import psycopg2
from flask import Flask
from psycopg2.extras import DictCursor

TEST_DB = 'postgres://bapi@localhost/test_db?connect_timeout=5&sslmode=disable'
app = Flask(__name__)

def get_id():
    len = 5
    id = ''.join(random.choices(string.ascii_letters + string.digits, k = len))
    return id

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/live', methods=['GET'])
def live():
    return "alive"


@app.route('/shorten/<string:url>', methods=['GET', 'POST'])
def shorten_url(url: str):
    # print("URL entered: "+ url)
    short_id = get_id()
    query = """
    insert into urls(original_url, short_id) values(%s, %s);
    """
    with psycopg2.connect(TEST_DB) as conn:
        with conn.cursor() as cur:
            cur.execute(query, (url, short_id ))
            conn.commit()

    return f"Shortened URL: {short_id}"


@app.route('/expand/<string:id>')
def expand_url(id: str):
    query = """
    select original_url from urls where short_id = %s;
    """
    with psycopg2.connect(TEST_DB) as conn:
        with conn.cursor() as cur:
            cur.execute(query, (id, ))
            original_url = cur.fetchone()[0]
    return original_url
          


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
