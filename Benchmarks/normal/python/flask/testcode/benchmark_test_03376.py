# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest03376():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = FormData(payload=secret_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
