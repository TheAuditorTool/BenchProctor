# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest40206():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    eval(str(data))
    return jsonify({"result": "success"})
