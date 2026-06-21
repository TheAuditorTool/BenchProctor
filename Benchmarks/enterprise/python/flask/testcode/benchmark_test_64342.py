# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest64342():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
