# SPDX-License-Identifier: Apache-2.0
import secrets
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest05172():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
