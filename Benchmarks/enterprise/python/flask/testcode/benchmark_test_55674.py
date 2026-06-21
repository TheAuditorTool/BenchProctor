# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest55674():
    raw_body = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
