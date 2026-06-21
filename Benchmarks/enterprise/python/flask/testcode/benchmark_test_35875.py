# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest35875():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = FormData(payload=secret_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
