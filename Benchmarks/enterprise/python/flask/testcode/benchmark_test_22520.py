# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import time


def to_text(value):
    return str(value).strip()

def BenchmarkTest22520():
    field_value = request.form.get('field', '')
    data = to_text(field_value)
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
