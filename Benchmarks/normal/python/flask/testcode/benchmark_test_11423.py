# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest11423():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
