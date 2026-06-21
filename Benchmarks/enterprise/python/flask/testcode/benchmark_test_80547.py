# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest80547():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
