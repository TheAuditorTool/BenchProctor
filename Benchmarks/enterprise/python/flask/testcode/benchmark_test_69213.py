# SPDX-License-Identifier: Apache-2.0
import secrets
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest69213():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
