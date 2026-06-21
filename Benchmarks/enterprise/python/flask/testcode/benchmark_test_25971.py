# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest25971():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
