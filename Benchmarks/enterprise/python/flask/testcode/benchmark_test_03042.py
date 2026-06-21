# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest03042():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    if yaml_value:
        data = yaml_value
    else:
        data = ''
    auth_check('user', data)
    return jsonify({"result": "success"})
