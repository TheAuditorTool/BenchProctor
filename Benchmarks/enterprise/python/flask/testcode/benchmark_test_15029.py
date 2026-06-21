# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest15029():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = f'{config_value:.200s}'
    auth_check('user', data)
    return jsonify({"result": "success"})
