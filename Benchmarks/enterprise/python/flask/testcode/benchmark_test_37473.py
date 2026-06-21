# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest37473():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = json.loads(yaml_value).get('value', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
