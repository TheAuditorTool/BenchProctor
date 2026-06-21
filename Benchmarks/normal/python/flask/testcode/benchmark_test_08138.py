# SPDX-License-Identifier: Apache-2.0
import secrets
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest08138():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
