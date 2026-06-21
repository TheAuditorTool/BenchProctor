# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest20069():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
