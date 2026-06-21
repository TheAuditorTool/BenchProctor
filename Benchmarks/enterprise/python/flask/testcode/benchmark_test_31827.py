# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest31827():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
