# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest02836():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
