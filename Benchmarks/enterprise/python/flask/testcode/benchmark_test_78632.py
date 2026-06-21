# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from app_runtime import db


_shared_counter_lock = threading.Lock()

def BenchmarkTest78632():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with _shared_counter_lock:
        globals()['counter'] = int(comment_value)
    return jsonify({"result": "success"})
