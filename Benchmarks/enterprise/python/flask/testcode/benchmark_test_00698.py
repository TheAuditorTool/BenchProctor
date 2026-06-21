# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest00698():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
