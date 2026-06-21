# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest77046():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
