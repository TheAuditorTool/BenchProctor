# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest13461():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
