# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from app_runtime import db


_shared_counter_lock = threading.Lock()

def BenchmarkTest01925():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
