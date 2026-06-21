# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import time


def ensure_str(value):
    return str(value)

def BenchmarkTest12651():
    field_value = request.form.get('field', '')
    data = ensure_str(field_value)
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
