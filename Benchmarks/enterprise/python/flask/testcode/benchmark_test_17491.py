# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest17491():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = str(prop_value).replace('\x00', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
