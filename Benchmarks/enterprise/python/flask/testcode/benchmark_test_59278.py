# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from app_runtime import db


_shared_counter_lock = threading.Lock()

def BenchmarkTest59278():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
