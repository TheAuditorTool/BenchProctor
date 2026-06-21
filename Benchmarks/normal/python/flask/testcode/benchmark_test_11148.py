# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest11148():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = str(file_value).replace('\x00', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
