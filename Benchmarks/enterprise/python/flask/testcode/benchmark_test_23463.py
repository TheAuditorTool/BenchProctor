# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest23463():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = bytes.fromhex(file_value).decode('utf-8', 'ignore')
    auth_check('user', data)
    return jsonify({"result": "success"})
