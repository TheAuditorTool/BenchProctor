# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest00733():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
