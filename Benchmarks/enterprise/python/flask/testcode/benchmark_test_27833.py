# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest27833():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
