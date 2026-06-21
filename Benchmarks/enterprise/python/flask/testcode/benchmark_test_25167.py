# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest25167():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
