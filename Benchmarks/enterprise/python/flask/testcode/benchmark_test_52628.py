# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest52628():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    if config_value:
        data = config_value
    else:
        data = ''
    auth_check('user', data)
    return jsonify({"result": "success"})
