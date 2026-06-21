# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest33104():
    secret_value = 'config_secret_test_abc123'
    data = FormData(payload=secret_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
