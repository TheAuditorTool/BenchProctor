# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest80868():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = yaml_value if yaml_value else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})
