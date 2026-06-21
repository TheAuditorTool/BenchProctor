# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest24662():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = json.loads(config_value).get('value', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
