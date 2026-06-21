# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest68183():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    prefix = ''
    data = prefix + str(config_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
