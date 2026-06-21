# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51531():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
