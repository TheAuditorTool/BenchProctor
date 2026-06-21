# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest64070():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    prefix = ''
    data = prefix + str(yaml_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
