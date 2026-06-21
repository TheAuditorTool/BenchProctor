# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest40473():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
