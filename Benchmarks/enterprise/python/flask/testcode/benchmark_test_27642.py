# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest27642():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    auth_check('user', prop_value)
    return jsonify({"result": "success"})
