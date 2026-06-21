# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest16687():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data, _sep, _rest = str(file_value).partition('\x00')
    auth_check('user', data)
    return jsonify({"result": "success"})
