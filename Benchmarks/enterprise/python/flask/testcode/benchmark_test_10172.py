# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db, auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10172():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    auth_check('user', data)
    return jsonify({"result": "success"})
