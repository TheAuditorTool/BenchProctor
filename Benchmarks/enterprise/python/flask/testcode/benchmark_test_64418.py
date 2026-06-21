# SPDX-License-Identifier: Apache-2.0
import base64
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest64418():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = base64.b64decode(file_value).decode('utf-8', 'ignore')
    auth_check('user', data)
    return jsonify({"result": "success"})
