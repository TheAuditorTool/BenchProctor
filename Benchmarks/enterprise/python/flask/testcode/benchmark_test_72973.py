# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest72973():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    return jsonify({'error': 'An internal error occurred'}), 500
