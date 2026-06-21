# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest08262():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
