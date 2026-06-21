# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest24705():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
