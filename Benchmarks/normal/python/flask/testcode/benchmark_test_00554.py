# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest00554():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    return jsonify({'error': 'An internal error occurred'}), 500
