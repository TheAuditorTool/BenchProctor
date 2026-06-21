# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import re
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest06223():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
