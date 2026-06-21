# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from app_runtime import db


_shared_counter_lock = threading.Lock()

def BenchmarkTest25100():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
