# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest33230():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    return jsonify({'error': 'An internal error occurred'}), 500
