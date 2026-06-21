# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest35912():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = to_text(config_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
