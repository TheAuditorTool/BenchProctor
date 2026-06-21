# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest16816():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    auth_check('user', yaml_value)
    return jsonify({"result": "success"})
