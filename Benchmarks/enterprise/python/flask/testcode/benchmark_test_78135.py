# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest78135():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = str(config_value).replace('\x00', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
