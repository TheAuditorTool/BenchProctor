# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09256():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
