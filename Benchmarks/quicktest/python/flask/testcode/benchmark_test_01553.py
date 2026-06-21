# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from app_runtime import db


_shared_counter_lock = threading.Lock()

def BenchmarkTest01553():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
