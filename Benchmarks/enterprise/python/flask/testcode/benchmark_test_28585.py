# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import runpy


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest28585():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    if time.time() > 1000000000:
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
