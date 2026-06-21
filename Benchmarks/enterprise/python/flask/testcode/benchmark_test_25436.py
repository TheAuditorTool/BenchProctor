# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest25436():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = '{}'.format(file_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
