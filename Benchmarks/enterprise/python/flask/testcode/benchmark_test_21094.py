# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db, auth_check


request_state: dict[str, str] = {}

def BenchmarkTest21094():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    auth_check('user', data)
    return jsonify({"result": "success"})
