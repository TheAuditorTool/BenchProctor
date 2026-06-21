# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


_shared_counter_lock = threading.Lock()

def BenchmarkTest33941():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
