# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest41816():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = '%s' % str(prop_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
