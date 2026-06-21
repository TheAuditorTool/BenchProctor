# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17391():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
