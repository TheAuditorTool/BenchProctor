# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest75446():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
