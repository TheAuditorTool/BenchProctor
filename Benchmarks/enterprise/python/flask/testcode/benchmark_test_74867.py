# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest74867():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = FormData(payload=yaml_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
