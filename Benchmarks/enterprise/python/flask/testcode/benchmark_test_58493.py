# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest58493():
    host_value = request.headers.get('Host', '')
    data = handle(host_value)
    if time.time() > 1000000000:
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
