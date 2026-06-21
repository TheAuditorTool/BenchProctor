# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest77766():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = FormData(payload=secret_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
