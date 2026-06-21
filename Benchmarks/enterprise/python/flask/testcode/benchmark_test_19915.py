# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest19915():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
