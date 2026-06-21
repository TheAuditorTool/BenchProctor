# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest50729():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    auth_check('user', config_value)
    return jsonify({"result": "success"})
