# SPDX-License-Identifier: Apache-2.0
import secrets
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest44284():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
