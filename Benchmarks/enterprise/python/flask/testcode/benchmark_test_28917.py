# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest28917():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
