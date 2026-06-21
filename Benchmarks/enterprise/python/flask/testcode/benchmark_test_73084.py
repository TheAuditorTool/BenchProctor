# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest73084():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(prop_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
