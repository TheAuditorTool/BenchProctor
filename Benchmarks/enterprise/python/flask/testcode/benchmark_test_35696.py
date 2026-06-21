# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35696():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
