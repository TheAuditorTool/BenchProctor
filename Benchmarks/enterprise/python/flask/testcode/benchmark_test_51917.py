# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest51917():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
