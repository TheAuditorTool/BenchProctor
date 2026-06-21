# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33019():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
