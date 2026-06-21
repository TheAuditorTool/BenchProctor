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

def BenchmarkTest72186():
    field_value = request.form.get('field', '')
    data = handle(field_value)
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return jsonify({"result": "success"})
