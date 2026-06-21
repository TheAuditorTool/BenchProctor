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

def BenchmarkTest08815():
    user_id = request.args.get('id', '')
    data = handle(user_id)
    def _primary():
        os.system('echo ' + str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
