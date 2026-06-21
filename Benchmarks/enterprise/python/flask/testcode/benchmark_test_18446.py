# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest18446():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = to_text(db_value)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return jsonify({"result": "success"})
