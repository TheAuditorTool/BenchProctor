# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest80663():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    prefix = ''
    data = prefix + str(prop_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
