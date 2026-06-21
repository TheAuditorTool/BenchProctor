# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest12301():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
