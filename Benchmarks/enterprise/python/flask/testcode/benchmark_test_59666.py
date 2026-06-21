# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest59666():
    auth_header = request.headers.get('Authorization', '')
    data = to_text(auth_header)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
