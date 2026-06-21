# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest79930():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
