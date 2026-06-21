# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import time
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest56589():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    if time.time() > 1000000000:
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
