# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest50101():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
