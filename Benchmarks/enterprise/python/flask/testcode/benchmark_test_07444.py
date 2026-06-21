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

def BenchmarkTest07444():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    checked_path = os.path.normpath(data)
    os.unlink('/var/app/data/' + str(checked_path))
    return jsonify({"result": "success"})
