# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00123():
    origin_value = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
