# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59136():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
