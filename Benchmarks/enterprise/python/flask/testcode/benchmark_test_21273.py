# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest21273():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
