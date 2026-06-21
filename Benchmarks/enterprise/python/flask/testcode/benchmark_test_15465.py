# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15465():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
