# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest79953():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    eval(compile("subprocess.run([str(data), '--status'], shell=False)", '<sink>', 'exec'))
    return jsonify({"result": "success"})
