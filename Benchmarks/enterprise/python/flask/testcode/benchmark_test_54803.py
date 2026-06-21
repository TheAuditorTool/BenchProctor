# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest54803():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = json.loads(file_value).get('value', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
