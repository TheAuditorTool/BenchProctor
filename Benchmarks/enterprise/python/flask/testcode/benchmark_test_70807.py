# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest70807():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = coalesce_blank(yaml_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
