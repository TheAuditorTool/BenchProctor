# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest26047():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = coalesce_blank(file_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
