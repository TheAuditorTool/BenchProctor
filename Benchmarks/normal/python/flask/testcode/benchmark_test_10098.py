# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest10098():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    auth_check('user', file_value)
    return jsonify({"result": "success"})
