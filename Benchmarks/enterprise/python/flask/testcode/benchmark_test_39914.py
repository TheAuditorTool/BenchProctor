# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest39914(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
