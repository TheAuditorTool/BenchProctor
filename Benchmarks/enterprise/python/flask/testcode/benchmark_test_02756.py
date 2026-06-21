# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest02756():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
