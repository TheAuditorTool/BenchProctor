# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10495():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
