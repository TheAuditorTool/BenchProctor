# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest07054():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
