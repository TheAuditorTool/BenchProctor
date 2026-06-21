# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest80164():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = prop_value if prop_value else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})
