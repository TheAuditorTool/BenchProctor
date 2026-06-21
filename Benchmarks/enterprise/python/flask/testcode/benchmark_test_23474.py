# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import time
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest23474():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})
