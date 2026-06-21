# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest10875():
    field_value = request.form.get('field', '')
    data = handle(field_value)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
