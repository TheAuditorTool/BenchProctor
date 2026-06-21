# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest40774():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
