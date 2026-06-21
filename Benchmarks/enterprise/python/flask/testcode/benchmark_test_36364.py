# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
from app_runtime import auth_check


def BenchmarkTest36364():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    try:
        data = json.loads(yaml_value).get('value', yaml_value)
    except (json.JSONDecodeError, AttributeError):
        data = yaml_value
    auth_check('user', data)
    return jsonify({"result": "success"})
