# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest48218():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    return str(data), 200, {'Content-Type': 'text/html'}
