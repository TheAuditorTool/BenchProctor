# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest38447():
    user_id = request.args.get('id', '')
    data = handle(user_id)
    processed = data[:64]
    data = bytearray(int(processed) if str(processed).isdigit() else 0)
    return jsonify({"result": "success"})
