# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
from flask import request, jsonify
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest23680():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
