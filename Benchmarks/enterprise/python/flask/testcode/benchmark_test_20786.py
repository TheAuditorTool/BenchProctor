# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import time
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest20786():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
