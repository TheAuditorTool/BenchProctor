# SPDX-License-Identifier: Apache-2.0
import jwt
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest04763():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = FormData(payload=secret_value).payload
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return jsonify({"result": "success"})
