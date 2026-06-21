# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest02212():
    user_id = request.args.get('id', '')
    data = handle(user_id)
    if os.environ.get("APP_ENV", "production") != "test":
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})
