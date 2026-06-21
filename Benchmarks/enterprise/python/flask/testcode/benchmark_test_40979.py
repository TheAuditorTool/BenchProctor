# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest40979():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
