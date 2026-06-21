# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17030():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
