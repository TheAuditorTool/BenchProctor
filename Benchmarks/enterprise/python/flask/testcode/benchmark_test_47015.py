# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest47015():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = FormData(payload=forwarded_ip).payload
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
