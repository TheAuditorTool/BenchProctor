# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest40769():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
