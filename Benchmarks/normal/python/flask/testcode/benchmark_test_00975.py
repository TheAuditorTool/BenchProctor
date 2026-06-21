# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest00975():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = ensure_str(file_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
