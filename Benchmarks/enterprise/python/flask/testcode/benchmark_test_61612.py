# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest61612():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
