# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest08052():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
