# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest80884():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = relay_value(prop_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
