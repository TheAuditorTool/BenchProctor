# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest40563():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    parts = []
    for token in str(prop_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    auth_check('user', data)
    return jsonify({"result": "success"})
