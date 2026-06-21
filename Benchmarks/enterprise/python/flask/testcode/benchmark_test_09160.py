# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest09160():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})
