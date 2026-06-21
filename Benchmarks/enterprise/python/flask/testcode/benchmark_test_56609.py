# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest56609():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
